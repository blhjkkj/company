from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic,Xinw,About
from comment.models import Comment
from comment.forms import CommentForm
from django.utils import timezone
from datetime import datetime
def 首页(request):
    """百龄花健康科技的主页"""
    return render(request,'company/首页.html')

def 公司简介(request):
    abouts=About.objects.all()
    context={'abouts':abouts}
    return render(request,'company/公司简介.html',context)
def 体质评测(request):
    return render(request,'company/体质评测.html')

def 分类资讯(request):
    #显示所有分类及全部分类下的资讯,2022年6月22日修改,在model中见方法1
    topics=Topic.objects.all()
    context={'topics':topics}
    return render(request,'company/分类资讯.html',context)

def topic(request,topic_id):
    #显示单个分类下所有文章
    topic=Topic.objects.get(id=topic_id)
    xinws=topic.xinw_set.all().order_by('-date_added')
    #latests=xinws.filter(published_date__lte=timezone.now()).reverse()[:3]
    context={'topic':topic,'xinws':xinws}
    return render(request,'company/topic.html',context)
def datil(request,id):#加入exclude(id=xinw_id)后实现目标
    xinw=Xinw.objects.get(id=id)#获取新闻id
    xinw.click_num=+1
    xinw.save()
    comments=Comment.objects.filter(xinw=id)
    comment_form=CommentForm()
    #获取分类标签
    topic=Xinw.objects.get(id=id).topic
    about_xinws_list=[]
    
    #分类项下文章定义相关文章
    #about_xinws_list=topic.xinw_set.exclude(id=xinw_id)filter
    for about_xinw in topic.xinw_set.all().exclude(id=id):
        #文章不存在list里且少于4篇，则放入list中
        if about_xinw not in about_xinws_list and len(about_xinws_list)<4:
            about_xinws_list.append(about_xinw)
    #print("about_xinws_list:",about_xinws_list)
    context={'topic':topic, 'xinw':xinw,'about_xinws_list':about_xinws_list,'comment_form':comment_form,'comments':comments}
    return render(request,'company/datil.html',context)

def about(request):
    about = About.objects.all()
    return render(request,'about.html',{'about':about})

