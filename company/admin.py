from django.contrib import admin
# Register your models here.
from .models import Topic,Xinw,About
from django import forms
#ckeditor
from ckeditor.widgets import CKEditorWidget
class XinwInline(admin.TabularInline):
    model=Xinw
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):

    list_display=('caption','desc','date_added')
   
admin.site.register(About)
class XinwAdmin(admin.ModelAdmin):
    """文章详情管理"""
    list_display=('caption','topic','author','origin','date_added',)
    list_filter=('date_added','author','topic')
    search_fields=('caption','author','topic','date_added',)
    #list_editable=('is_hot',)
    list_display_links=('author','caption','topic')
admin.site.register(Xinw,XinwAdmin)
admin.site.site_header='杭州百龄花健康科技有限公司'
admin.site.index_title='网站管理后台'