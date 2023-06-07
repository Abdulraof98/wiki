
from django.contrib import admin
from django.urls import path, include,re_path
from .views import ArticleList,ArtilceDetail,ArticleVersionList,ArticleVersionDetail,ArticleVersions

urlpatterns = [
    path("article/", ArticleList.as_view()), # Articles with their latest version
    path("article/<int:pk>", ArtilceDetail.as_view()), # One Article with lastest Version
    path("article-version/", ArticleVersionList.as_view()), # List of all versions
    path("article-version/<int:pk>", ArticleVersionDetail.as_view()), # One article version
    path("article-versions", ArticleVersions.as_view()), #list of all articles with their versions
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
