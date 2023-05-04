from django.db import models
from django.conf import settings

class Language(models.Model):
    language_name = models.CharField(max_length=100)
    language_code = models.CharField(max_length=5)

class Article(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    

class UserLanguage(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

class ArticleLanguage(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

class ArticleVersion(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_of_edit = models.DateTimeField(auto_now=True)
    description = models.TextField()
    refrences = models.CharField(max_length=255)
    body = models.TextField()
    keywords = models.CharField(max_length=100)
    verified = models.BooleanField()
    #verified by ?

class ActivityType(models.Model):
    value = models.CharField(max_length=1)


class UserActivity(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
    type_of_activity = models.IntegerField()
    date_of_activity = models.DateTimeField() # update or only crreate ?

class Comment(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

class Report(models.Model):
    details = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    version_id = models.ForeignKey(ArticleVersion, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    verified = models.BooleanField()

