
from django.contrib import admin
from django.urls import path, include,re_path
from .views import ArticleList,ArtilceDetail,ArticleVersionList,ArticleVersionDetail,ArticleVersions,CommentList,LikesView, ReportsView
from .views import SearchView, UserActivityList
urlpatterns = [
    path("article/", ArticleList.as_view()), # Articles with their latest version
    path("article/<int:pk>", ArtilceDetail.as_view()), # One Article with lastest Version
    path("article-version/", ArticleVersionList.as_view()), # List of all versions
    path("article-version/<int:pk>", ArticleVersionDetail.as_view()), # One article version
    path("article-versions", ArticleVersions.as_view()), #list of all articles with their versions
    path("like/<int:pk>", LikesView.as_view()), 
    path("report/<int:pk>", ReportsView.as_view()), 
    # path("comment/<int:pk>", Comment.as_view()),
    path('comments/<int:pk>', CommentList.as_view()),
    path('search',SearchView.as_view()),
    path('user-activites/<int:pk>',UserActivityList.as_view())
]
