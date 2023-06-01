from rest_framework import serializers
from .models import Article
from .models import ArticleVersion
from .models import UserActivity
from .models import Report
from .models import Comment
from .models import ActivityType


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','user_id']

class ArticleVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleVersion
        fields = '__all__'
class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = '__all__'
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = '__all__'