from django.shortcuts import render
from .models import Article, UserActivity,Comment,ActivityType,ArticleVersion
from .serializers import ArticleSerializer,ArticleVersionSerializer,UserActivitySerializer
from .serializers import CommentSerializer,ArticalVersionSerializer__2
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
# from rest_framework import viewsets
# For react app ---
# def index(request):
# 	return render(request, 'index.html')
# Create your views here.

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
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleVersionList(APIView):
    def get(self, request):
        queryset = ArticleVersion.objects.all()
        serializer = ArticleVersionSerializer(queryset, many=True, context={'context': request})
        return Response(serializer.data)
    
    def post(self, request):
        print("DDDDD")
        print(request.data)
        
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
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
        serializer = ArticleVersionSerializer(article_version, dat=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        article_verion = get_object_or_404(ArticleVersion, pk=pk)
        article_verion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# class UserActivityList(APIView):
#     def get(self, request,pk=None):
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
