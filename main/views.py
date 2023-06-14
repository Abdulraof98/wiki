from django.shortcuts import render
from .models import Article, UserActivity, Like, Share, Comment, Report, ActivityType, ArticleVersion
from .serializers import ArticleSerializer, ArticleVersionSerializer, UserActivitySerializer
from .serializers import CommentSerializer, ArticalVersionSerializer__2
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from accounts.models import CustomUser
from accounts.serializers import UserSerializer
import json
from django.db import transaction
from django.forms.models import model_to_dict
from django.utils import timezone
from django.db.models import Q
# from rest_framework import viewsets
# For react app ---
# def index(request):
# 	return render(request, 'index.html')
# Create your views here.

current_user = CustomUser.objects.get(id=1)
def create_user_activity(action,article):
    act_type = ActivityType.objects.filter(value = action).first()
    current_user = CustomUser.objects.get(id=1)
    user_activity = UserActivity.objects.create(article_id=article,user_id= current_user,type_of_activity=act_type)
    if user_activity:
        return True
    return False

class SearchView(APIView):
    def get(self,request):
        data = request.data
        print(data['search'])
        articles = ArticleVersion.objects.filter(title__icontains=data['search'])
        serializer = ArticleVersionSerializer(articles,many=True)
        return Response(serializer.data)


class ArticleList(APIView):
    def get(self, request):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = ArticleSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArtilceDetail(APIView):
    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            with transaction.atomic():

                article = get_object_or_404(Article, pk=pk)
                serializer = ArticleSerializer(article, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                create_user_activity('update',article.id)
                
        except Exception as e:
            
            return e
        return Response(serializer.data)
    
    def patch(self, request, pk):
        # Retrieve the object to be updated
        obj = Article.objects.get(pk=pk)

        # Apply the partial updates from the request data
        serializer = ArticleSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class ArticleVersionList(APIView):
    def get(self, request):
        queryset = ArticleVersion.objects.all()
        serializer = ArticleVersionSerializer(queryset, many=True, context={'context': request})
        return Response(serializer.data)
    def post(self, request):

        try:
            with transaction.atomic():
                data = request.data
                user = CustomUser.objects.get(id=data['user_id'])
                current_user = CustomUser.objects.get(id=1)
                article = Article()
                article_v = ArticleVersion()
                article.user_id = user
                article.save()
                article_v.article_id = article
                article_v.title = data['article_version']['title']
                article_v.user_id = current_user
                article_v.description = data['article_version']['description']
                article_v.refrences = data['article_version']['refrences']
                article_v.body = data['article_version']['body']
                article_v.keywords = data['article_version']['keywords']
                article_v.save()
                create_user_activity('create',article)
            
        except Exception as e:
            # Rollback the transaction if an exception occurs
            
            raise e
        
        version_dict = model_to_dict(article_v)
        return JsonResponse(version_dict, safe=False)
    
class ArticleVersions(APIView):
    def get(self,request):
        queryset = Article.objects.all()
        serializer = ArticalVersionSerializer__2(queryset, many=True, context={'context': request})
        return Response(serializer.data)
    
class ArticleVersionDetail(APIView):
    def get(self, request, pk):
        # article_version = get_object_or_404(ArticleVersion, pk=pk)
        article_version = ArticleVersion.objects.filter(article_id=pk).order_by('-date_of_edit').first()
        serializer = ArticleVersionSerializer(article_version)
        return Response(serializer.data)
    
    def put(self, request, pk):
        article_version = get_object_or_404(ArticleVersion, pk=pk)

        try:
            with transaction.atomic():
                data = request.data
                # user = CustomUser.objects.get(id=data['user_id'])
                current_user = CustomUser.objects.get(id=1)
                article = get_object_or_404(Article, pk=pk)
                article_v = get_object_or_404(ArticleVersion, pk=pk)
                # article.user_id = user
                # article.save()
                # article_v.article_id = article
                article_v.title = data['title']
                # article_v.user_id = current_user.id
                article_v.description = data['description']
                article_v.refrences = data['refrences']
                article_v.body = data['body']
                article_v.keywords = data['keywords']
                article_v.save()
                create_user_activity('update',article) 
                
            
        except Exception as e:

            
            raise e
        
        version_dict = model_to_dict(article_v)
        return JsonResponse(version_dict, safe=False)
    
    def delete(self, request, pk):
        article_verion = get_object_or_404(ArticleVersion, pk=pk)
        article_verion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CommentList(APIView):
    def get(self,request,pk):

            # article = get_object_or_404(Article, pk=pk)
            comments = Comment.objects.filter(article_id=pk) 
            serializer = CommentSerializer(comments, many=True)
            return Response({'comments': serializer.data})
        # return Response({"user_id":request.user})
    def post(self,request,pk):
        try:
            with transaction.atomic():
                article = get_object_or_404(Article, pk=pk)
                Comment.objects.create(article_id=article,user_id= current_user,comment=request.data['comment'])
                create_user_activity('comment',article)
            
        except Exception as e:
            
            raise e
        return JsonResponse({"Details": "Comment Created Successfully!"}, safe=False)
class LikesView(APIView):
    def get(self,request,pk):
        pass
    def post(self,request,pk):
        try:
            with transaction.atomic():
                
                # current_user = request.user.id
                user = CustomUser.objects.get(id=current_user.id)
                article = Article.objects.get(id=pk)
                
                if Like.objects.filter(user_id=current_user.id).exists():
                    print("SSS")
                    return JsonResponse({'status':False})
                Like.objects.create(user = user, article = article)
                create_user_activity('like',article)
                
        except Exception as e:
            response_data = {
                  'error': str(e)  # Convert the TypeError object to a string
            }
            return JsonResponse(response_data)
        
        return JsonResponse({'status':True}, safe=False)
class ReportsView(APIView):
    def get(self,request,pk):
        pass
    def post(self,request,pk):
        try:
            with transaction.atomic():
                # current_user = request.user.id
                user = CustomUser.objects.get(id=current_user.id)
                article = Article.objects.get(id=pk)
                create_user_activity('report',article.id)
                if Report.objects.filter(user_id=current_user.id).exists():
                    return JsonResponse({'status':False})
                Report.objects.create(user = user, article = article)
                
        except Exception as e:
            
            return e
        
        return JsonResponse({'status':True})
class UserActivityList(APIView):
    def get(self, request,pk=None):
        user = CustomUser.objects.get(id=pk)
        # Get the activities of the current user that 
        # its ID is forignKey in useractivity table
        data = request.data
        if data['search']:
            activities = UserActivity.objects.filter(Q(user_id=user.id) & Q(value_icontains=data['search']))
        else:
            activities = user.useractivity_set.all() 
        serializer = UserActivitySerializer(activities,many=True)
        return Response(serializer.data)
        
        try:
           if activities: 
            serializer = UserActivitySerializer(activities,many=True, context={'request': request}) #many records
            data  = serializer.data
            return JsonResponse({'UserActivity':data},safe=False)
        except UserActivity.DoesNotExist:
            return Response({'message': 'UserActivity not found.'}, status=404)
    
# class ArticleAPIView(APIView):
#     def get(self, request, pk=None):
        
#             datas = Article.objects.all()
#             serializer = ArticleSerializer(datas,many=True)
#             return JsonResponse({'article':serializer.data})
#             # if pk:
#             #     article = get_object_or_404(Article, pk=pk)
# class SingleAPIView(APIView):
#     def get(self, request,pk):
#         if pk:
#             article = get_object_or_404(Article, pk=pk)
#             # datas = ArticleVersion.objects.get(id=pk)
#             serializer = ArticleSerializer(article)
#             return JsonResponse({'article':serializer.data})
        
# class VersionsAPIView(APIView):
#      def get(self,request,pk):
#           if pk:
#             versions = ArticleVersion.objects.filter(article_id=pk)
#             serializer = ArticleVersionSerializer(versions,many=True) #many records
#             return JsonResponse({'versions':serializer.data})
          

# class UserActivityAPIView(APIView):
#     def get(self, request,pk):
#         user = CustomUser.objects.get(id=pk)
#         # Get the activities of the current user that 
#         # its ID is forignKey in useractivity table
#         activities = user.useractivity_set.all()
#         try:
#            if activities: 
#             serializer = UserActivitySerializer(activities,many=True, context={'request': request}) #many records
#             data  = serializer.data
#             return JsonResponse({'UserActivity':data},safe=False)
#         except UserActivity.DoesNotExist:
#             return Response({'message': 'UserActivity not found.'}, status=404)
    
    
#     # @transaction.atomic
#     def post(self, request):
#         with transaction.atomic():

#             serializer = UserActivitySerializer(data=request.data)
#             # This is for post method
#             if serializer.is_valid() :
#                 serializer.save()
#                 return Response(serializer.data, status=200)

#         return Response(serializer.errors, status=400)
    
# class CommentAPIView(APIView):
#     def get(self,request,pk=None):
#         if pk:
#             comments = Comment.objects.get(id=pk) 
#             serializer = CommentSerializer(comments)
#         else:
#              comments = Comment.objects.all()
#              serializer = CommentSerializer(comments, many=True)
#         return Response({'comments': serializer.data})
#         # return Response({"user_id":request.user})
#     def post(self,request):

#         comment = Comment.objects.get(id=request.data['id']) 
#         user_id = comment.user_id
#         user = request.user
#         return Response({"user_id":user, "username":request.username})
   
# @api_view(['GET','POST'])
# # @api_view('GET')
# def articles(request):
#     #get all the drinks
#     #serialize them
#     #return json
#     if request.method == 'GET':
#         datas = Article.objects.all()
#         serializer = ArticleSerializer(datas,many=True)
#         return JsonResponse({'article':serializer.data})
#     if request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET','PUT','DELETE'])
# def drink_detial(request, id):

#     try:
#         drink = Drink.objects.get(pk=id)
#     except Drink.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = DrinkSerializer(drink)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = DrinkSerializer(drink, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         drink.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
