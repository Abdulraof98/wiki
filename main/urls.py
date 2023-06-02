
from django.contrib import admin
from django.urls import path, include,re_path
from .views import ArticleAPIView
from .views import SingleAPIView
from .views import VersionsAPIView,UserActivityAPIView

urlpatterns = [
    path('', ArticleAPIView.as_view()),
    path('<int:pk>/', SingleAPIView.as_view()),
    path('versions/<int:pk>/', VersionsAPIView.as_view()),
    path('user-activites/<int:param>/', UserActivityAPIView.as_view()),
]
