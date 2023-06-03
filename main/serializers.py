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
class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = '__all__'
class UserActivitySerializer(serializers.ModelSerializer):

    # the value of source should be same as an attr of the child class
    activity_type = ActivityTypeSerializer(source='type_of_activity', read_only=True) 
    class Meta:
        model = UserActivity
        fields =['user_id','article_id','type_of_activity','activity_type','date_of_activity']
        # depth = 1 #Recorsive loop to first parent
    
    # type_of_activity  = serializers.SerializerMethodField('activity_name')
    # def get_user_id(self,obj):
    #     # Custom logic to retrieve custom data
    #     # You can access request or view attributes through self.context
    #     id1 = self.context.get('activity_name')
    #     return id1
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'