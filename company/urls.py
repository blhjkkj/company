"""为’company'配置的URL模式"""
from django.urls import path
from . import views
app_name = 'company'
urlpatterns = [
    path('',views.首页,name='首页'),
    path('公司简介/', views.公司简介, name = '公司简介'),
    path('体质评测/', views.体质评测, name = '体质评测'),
    path('datil/<int:id>/',views.datil,name='datil'),
    path('分类资讯/<int:topic_id>/', views.topic, name="topic"),
    path('分类资讯/',views.分类资讯,name ='分类资讯'),
    
]