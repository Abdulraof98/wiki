
from django.contrib import admin
from django.urls import path, include,re_path
from .views import ArticleAPIView
from .views import SingleAPIView
from .views import ArticleList,ArtilceDetail,ArticleVersionList,UserActivityList,ArticleVersionDetail

urlpatterns = [
    path("article/", ArticleList.as_view()),
    path("article/<int:pk>", ArtilceDetail.as_view()),
    path("article-version/", ArticleVersionList.as_view()),
    path("article-version/<int:pk>", ArticleVersionDetail.as_view())
]
# urlpatterns = [
#     path('article', ArticleAPIView.as_view()),
#     path('article/<int:pk>/', SingleAPIView.as_view()),
#     path('version/<int:pk>/', VersionsAPIView.as_view()),
#     path('user-activites/<int:pk>/', UserActivityAPIView.as_view()),
#     path('comments/', CommentAPIView.as_view()),
#     path('comments/<int:pk>/', CommentAPIView.as_view()),
#     path('comments/user/<int:pk>/', CommentAPIView.as_view()),
# ]
