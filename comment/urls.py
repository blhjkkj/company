"""定义comment的URL模式"""
from django.urls import path
from . import views
app_name = 'comment'
urlpatterns = [
    #主页
    path('sharer_comment/<int:xinw_id>/', views.xinw_comment, name = 'xinw_comment'),
    path('commit_commit/<int:sharer_id>/', views.sharer_comment, name = 'commit_commit'),
    
   
]