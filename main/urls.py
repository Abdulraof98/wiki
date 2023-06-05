
from django.contrib import admin
from django.urls import path, include,re_path
from .views import ArticleList,ArtilceDetail,ArticleVersionList,ArticleVersionDetail,ArticleVersions

urlpatterns = [
    path("article/", ArticleList.as_view()),
    path("article/<int:pk>", ArtilceDetail.as_view(), name='article-detail'),
    path("article-version/", ArticleVersionList.as_view()),
    path("article-version/<int:pk>", ArticleVersionDetail.as_view()),
    path("article-versions", ArticleVersions.as_view()), #display all versions of an article
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
