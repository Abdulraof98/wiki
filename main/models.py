from django.db import models
from django.conf import settings

class Language(models.Model):
    language_name = models.CharField(max_length=100)
    language_code = models.CharField(max_length=5)

class Article(models.Model):
    # title = models.CharField(max_length=100)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user_id}'    
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
    def __str__(self):
        return f'{self.title} -- {self.description}'

class UserLanguage(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

class ArticleLanguage(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)


class ActivityType(models.Model):
    value = models.CharField(max_length=50)


class UserActivity(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
    type_of_activity = models.ForeignKey(ActivityType, on_delete =models.SET_NULL, null=True)
    date_of_activity = models.DateTimeField() # update or only create ?

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

