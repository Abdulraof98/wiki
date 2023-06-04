from rest_framework import serializers
from .models import Article
from .models import ArticleVersion
from .models import UserActivity
from .models import Report
from .models import Comment
from .models import ActivityType
import json


class ArticleVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleVersion
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    
    artical_detail = serializers.SerializerMethodField("_get_title_name")
    class Meta:
        model = Article
        fields = ['id','user_id','artical_detail']

    def _get_title_name(self,obj):
        article_versions = obj.articleversion_set.latest('date_of_edit')
        serializer = ArticleVersionSerializer(article_versions)
        return serializer.data
        # title_list = [article.title for article in article_versions]
        # return title_list
    
class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = '__all__'
class UserActivitySerializer(serializers.ModelSerializer):

    activity_name = serializers.SerializerMethodField("_get_type_name")

    def _get_type_name(self, driver_object):

        # Return (UserActivity)obj->type_of_activity->{(forignKey)(ActivityType)->value}
        return driver_object.type_of_activity.value
    class Meta:
        model = UserActivity
        fields =['user_id','article_id','type_of_activity','activity_name','date_of_activity']
        # depth = 1 #Recorsive loop to first parent

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'