from django.contrib import admin
<<<<<<< Updated upstream

# Register your models here.
=======
from .models import ArticleVersion, Article, ActivityType,Comment, Report, UserActivity
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id','created_date']

class ArticleVersionAdmin(admin.ModelAdmin):
    list_display = ['article_id','title', 'user_id','description']

class ActivityTypeAdmin(admin.ModelAdmin):
    list_display = ['id','value']

class UserActivityAdmin(admin.ModelAdmin):
    list_display = ['type_of_activity','article_id', 'user_id']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['article_id','comment', 'user_id']

class ReportAdmin(admin.ModelAdmin):
    list_display = ['details','user_id', 'version_id']

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleVersion, ArticleVersionAdmin)
admin.site.register(ActivityType,ActivityTypeAdmin)
admin.site.register(UserActivity,UserActivityAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Report,ReportAdmin)
>>>>>>> Stashed changes
