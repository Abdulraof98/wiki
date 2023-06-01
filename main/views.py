from django.shortcuts import render

from .models import Article, UserActivity
from .models import ArticleVersion
from .serializers import ArticleSerializer
from .serializers import ArticleVersionSerializer,UserActivitySerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from accounts.models import CustomUser
from accounts.serializers import UserSerializer
import json
from django.http import JsonResponse
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
    def get(self, request,param):
        user = CustomUser.objects.get(id=param)
        activities = user.useractivity_set.all()
        # return JsonResponse({"user":user,"activities":activities})
        # user_data = serializers.serialize('python', [user])[0]['fields']
        # activities_data = list(activities.values())

        # return JsonResponse({"user": user_data, "activities": activities_data})
        try:
           if activities: 
        #     userdetails = UserSerializer(user,data=request.data) 
            serializer = UserActivitySerializer(activities,many=True) #many records

            return JsonResponse({'UserActivity':serializer.data},safe=False)
        except UserActivity.DoesNotExist:
            return Response({'message': 'UserActivity not found.'}, status=404)

        serializer = UserActivitySerializer(activities, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)
    
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
