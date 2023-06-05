from rest_framework import serializers
from .models import Article
from .models import ArticleVersion
from .models import UserActivity
from .models import Report
from .models import Comment
from .models import ActivityType
from django.db import transaction

class ArticleVersionSerializer(serializers.ModelSerializer):
    verified = serializers.BooleanField(required=False)
    class Meta:
        model = ArticleVersion
        fields = ['id', 'title', 'date_of_edit', 'description', 'refrences', 'body', 'keywords', 'verified', 'user_id']

class ArticleSerializer(serializers.ModelSerializer):
    article_version = ArticleVersionSerializer()
    
    class Meta:
        model = Article
        fields = ['id', 'user_id', 'article_version']
    
    def create(self, validated_data):
        article_version_data = validated_data.pop('article_version')
        if article_version_data:
            with transaction.atomic():
                article = Article.objects.create(**validated_data)
                article_v = ArticleVersion.objects.create(article_id=article, **article_version_data)
                
        return article_v 






class ArticalVersionSerializer__2(serializers.ModelSerializer):
    
    
    artical_detail = serializers.SerializerMethodField("_get_title_name")
    class Meta:
        model = Article
        fields = ['id','user_id','artical_detail'] 

    def _get_title_name(self,obj):
        ArticleVersionSerializer
        # article_versions = obj.articleversion_set.all()
        article_versions = obj.article_version.all()

        serializer = ArticleVersionSerializer(article_versions, many=True)
        return serializer.data
    
 
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