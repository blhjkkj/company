from django.contrib import admin
# Register your models here.
from .forms import forms
from .models import Topic,Sharer
from comment.models import Comment
class CommentInline(admin.TabularInline):
    model=Comment
@admin.register(Sharer)
class SharerAdmin(admin.ModelAdmin):
    list_display=('capt','date_added','author','action')
    list_display_links=('capt','date_added','action','author')
    list_filter=('author','topic','date_added')
    inlines=[CommentInline] 
   
    #用登录名作为新分享的作者名
def has_change_permission(self, request, obj=None):
    has_class_permission = super(SharerAdmin, self).has_change_permission(request, obj)
    if not has_class_permission:
        return False
    if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
        return False
    return True
def queryset(self, request):
    if request.user.is_superuser:
        return Sharer.objects.all()
    return Sharer.objects.filter(author=request.user)
def save_model(self, request, obj, form, change):
    if not change:
        obj.author = request.user
    obj.save()

class SharerInline(admin.TabularInline):
    model=Sharer
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display=('text','owner','date_added')
    inlines=[SharerInline]