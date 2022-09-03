from django.contrib import admin
from mptt.admin import MPTTModelAdmin
# Register your models here.
from .forms import forms
from .models import Comment
admin.site.register(Comment,MPTTModelAdmin)
"""
@admin.register(Comment)
class TopicAdmin(admin.ModelAdmin):
    list_display=('user','parent','reply_to','content','created_date')"""