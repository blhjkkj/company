from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404  
from comment.models import Comment
from .models import Topic,Sharer
from .forms import TopicForm,SharerForm
from comment.forms import CommentForm

# Create your views here.


def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/健康笔记.html')
def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.all().order_by('date_added')#filter(owner=request.user)去除仅所者可看
    context ={'topics':topics}
    return render(request,'learning_logs/topics.html', context)
@login_required
def topic(request, topic_id):
    """显示单个主题及其所有的条目。"""
    topic =Topic.objects.get(id = topic_id)
    #确认请求的主题是否属于当前用户，并返回不同的内容
    if topic.owner != request.user:
        sharers= topic.sharer_set.filter(action='0').order_by('-date_added')        
    if topic.owner == request.user:
        sharers=topic.sharer_set.order_by('-date_added')
    context = {'topic':topic, 'sharers':sharers}
    return render(request, 'learning_logs/topic.html',context)
#def datil(request,sharer_id):
def datil(request,id):
    #sharer=Sharer.objects.get(id=sharer_id)#获取新闻id
    sharer=Sharer.objects.get(id=id)    
    #comments=sharer.comment_set.all().order_by('-created_date')
    comments=Comment.objects.filter(sharer=id)
    sharer.click_num=+1
    sharer.save()
    comment_form=CommentForm()
    topic=Sharer.objects.get(id=id).topic
    context={'comment_form':comment_form,'sharer':sharer,'topic':topic,'comments':comments}
    return render(request,'learning_logs/阅读全文.html',context)
@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        #未提交表单，创建一个新表单。
        form = TopicForm()
    else:
        #POST提交的数据：对数据进行处理。
        form = TopicForm(data = request.POST)
        if form.is_valid():
            new_topic = form.save(commit =False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    #显示空表单或指出表单数据无效
    context = {'form' : form}
    return render(request, 'learning_logs/new_topic.html', context)
@login_required
def new_sharer(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = SharerForm()
    else:
        form=SharerForm(data=request.POST)
        if form.is_valid():
            new_sharer=form.save(commit=False)
            new_sharer.topic =topic
            new_sharer.author=request.user
            new_sharer.save()
            return redirect('learning_logs:topic',topic_id=topic_id)
    context={'topic':topic, 'form' : form}
    return render(request,'learning_logs/new_sharer.html' , context)

@login_required
def edit_sharer(request,sharer_id):
    #编辑既有条目
    sharer = Sharer.objects.get(id = sharer_id)
    topic = sharer.topic
    #if sharer.author != request.user:
        #return HttpResponse('只有本文作者才能进行编辑，请返回上页，继续访问网站其他内容，或者点击评论按钮，发布您对本文的评论。')

    if request.method != 'POST':
        #初次请求，使用当前条目填充表单。
        form = SharerForm(instance = sharer)
    else:
        #POST提交的数据，对数据进行处理。
        form=SharerForm(instance = sharer, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect(sharer)
    context = {'sharer':sharer,'topic':topic,'form':form}
    return render(request, 'learning_logs/edit_sharer.html', context)
@login_required
def sharer_safe_delete(request, sharer_id):
    # 根据 id 获取需要删除的文章
    if request.method=='POST':
        sharer = Sharer.objects.get(id=sharer_id)
        # 调用.delete()方法删除文章
        sharer.delete()
    # 完成删除后返回文章列表
        return redirect("learning_logs:topics" )
    else:
        return HttpResponse('您没有权限或者请求错误。')

@login_required
def comment_safe_delete(request, id):
    print(request.POST)
    user = request.user
    sharer = get_object_or_404(Sharer, id=id)
    # 根据 id 获取需要删除的评论
    comments = Comment.objects.filter(sharer=id)
    for comment in comments:
        if request.method=='POST':
     
        # 调用.delete()方法删除文章
            comment.delete()
    # 完成删除后返回文章列表
        return redirect(sharer)
