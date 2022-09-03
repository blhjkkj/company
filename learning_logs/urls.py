"""定义learning_logs的URL模式"""
from django.urls import path
from . import views
app_name = 'learning_logs'
urlpatterns = [
    #主页
    path('index/', views.index, name = '健康笔记'),
    #显示所有主题（相当于二级页面）
    path('topics/', views.topics, name='topics'),
    #特定主题的详细页面（相当于三级页面）。
    path('topics/<int:topic_id>/', views.topic, name="topic"),
    #阅读全文的页面
    path('topic/<int:id>/',views.datil,name='阅读全文'),
    #用于添加新主题的页面。
    path('new_topic/', views.new_topic, name='new_topic'),  
    path('new_sharer/<int:topic_id>/',views.new_sharer,name='new_sharer'),
    path('edit_sharer/<int:sharer_id>/',views.edit_sharer,name='edit_sharer'),
    #path('sharer_delete/<int:id>/', views.sharer_delete, name='sharer_delete'),
    path('sharer_safe_delete/<int:sharer_id>/',views.sharer_safe_delete,name='sharer_safe_delete'),
    path('comment_safe_delete/<int:id>/',views.comment_safe_delete,name='comment_safe_delete'),
]