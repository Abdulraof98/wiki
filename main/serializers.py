from rest_framework import serializers
from .models import Article
from .models import ArticleVersion
from .models import UserActivity
from .models import Report
from .models import Like,Comment, Share
from .models import ActivityType
from django.db import transaction

# class CommentsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model:Comment
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
class ArticleVersionSerializer(serializers.ModelSerializer):
    verified = serializers.BooleanField(required=False)
    class Meta:
        model = ArticleVersion
        fields = ['id', 'article_id', 'title', 'date_of_edit', 'description', 'refrences', 'body', 'keywords', 'verified', 'user_id', 'status']

class ArticleSerializer(serializers.ModelSerializer):
    # article_version = ArticleVersionSerializer(many=True)
    article_version = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField('get_comment')
    likes = serializers.SerializerMethodField('get_like')
    shares = serializers.SerializerMethodField('get_share')
    
    class Meta:
        model = Article
        fields = ['id', 'user_id', 'article_version','likes','shares','comments']

    def get_article_version(self, article):
        latest_article_version = article.article_version.order_by('-id').first()
        if latest_article_version:
            return ArticleVersionSerializer(latest_article_version).data
        return None
    def get_comment(self,article):
        comments = article.comment.all()
        if comments:
            return CommentSerializer(comments, many=True).data
        else:
            return []
    def get_like(self,article):
        return article.like.count()
    
    def get_share(self,article):
        return article.share.count()
    
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
class LikeSerializer(serializers.ModelSerializer):
    class Mete:
        model = Like
        fields = '__all__'

class ShareSerializer(serializers.ModelSerializer):
    class Mete:
        model = Share
        fields = '__all__'
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
