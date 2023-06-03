
from django.contrib import admin
from django.urls import path, include,re_path
from .views import ArticleAPIView
from .views import SingleAPIView
from .views import VersionsAPIView,UserActivityAPIView,CommentAPIView


urlpatterns = [
    path('article', ArticleAPIView.as_view()),
    path('article/<int:pk>/', SingleAPIView.as_view()),
    path('versions/<int:pk>/', VersionsAPIView.as_view()),
    path('user-activites/<int:pk>/', UserActivityAPIView.as_view()),
    path('comments/', CommentAPIView.as_view()),
    path('comments/<int:pk>/', CommentAPIView.as_view()),
    path('comments/user/<int:pk>/', CommentAPIView.as_view()),
]
