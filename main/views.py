from django.shortcuts import render

from .models import Article, UserActivity,Comment,ActivityType
from .models import ArticleVersion
from .serializers import ArticleSerializer
from .serializers import ArticleVersionSerializer,UserActivitySerializer,CommentSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from accounts.models import CustomUser
from accounts.serializers import UserSerializer
import json
from django.http import JsonResponse
from django.db import transaction
# from rest_framework import viewsets
# For react app
# def index(request):
# 	return render(request, 'index.html')

class ArticleAPIView(APIView):
    def get(self, request):
        
            datas = ArticleVersion.objects.all()
            serializer = ArticleSerializer(datas,many=True)
            return JsonResponse({'article':serializer.data})
    
class SingleAPIView(APIView):
    def get(self, request,pk):
        if pk:
            datas = ArticleVersion.objects.get(id=pk)
            # ver = 
            # datas.artical_id
            serializer = ArticleVersionSerializer(datas)
            return JsonResponse({'article':serializer.data})
        
class VersionsAPIView(APIView):
     def get(self,request,pk):
          if pk:
            versions = ArticleVersion.objects.filter(article_id=pk)
            serializer = ArticleVersionSerializer(versions,many=True) #many records
            return JsonResponse({'versions':serializer.data})
from django.core import serializers

class UserActivityAPIView(APIView):
    def get(self, request,pk):
        user = CustomUser.objects.get(id=pk)
        # Get the activities of the current user that 
        # its ID is forignKey in useractivity table
        activities = user.useractivity_set.all()
        try:
           if activities: 
            activity_name="dummey"
            serializer = UserActivitySerializer(activities,many=True, context={'activity_name': activity_name}) #many records

            return JsonResponse({'UserActivity':serializer.data},safe=False)
        except UserActivity.DoesNotExist:
            return Response({'message': 'UserActivity not found.'}, status=404)
    # @transaction.atomic
    def post(self, request):
        with transaction.atomic():

            serializer = UserActivitySerializer(data=request.data)
            # This is for post method
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)
    
class CommentAPIView(APIView):
    def get(self,request,pk=None):
        if pk:
            comments = Comment.objects.get(id=pk) 
            serializer = CommentSerializer(comments)
        else:
             comments = Comment.objects.all()
             serializer = CommentSerializer(comments, many=True)
        return Response({'comments': serializer.data})
        # return Response({"user_id":request.user})
    def post(self,request):

        comment = Comment.objects.get(id=request.data['id']) 
        user_id = comment.user_id
        user = request.user
        return Response({"user_id":user, "username":request.username})
   
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
