"""为product配制URL模式"""
from django.urls import path
from . import views
app_name = 'product'
urlpatterns = [
    path('产品详情/<int:sp_id>/',views.products,name='产品详情'),
    path('sp_all/',views.sp_all,name='sp_all'),
    
]