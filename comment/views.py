from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Comment
from .forms import CommentForm
from learning_logs.models import Sharer
from company.models import Xinw
@login_required
def sharer_comment(request,sharer_id):
    print(request.POST)
    user = request.user
    content = request.POST.get('content')
    parent_id = request.POST.get('parent')
    sharer = get_object_or_404(Sharer, id=sharer_id)
    if parent_id:
        parent = get_object_or_404(Comment, id=parent_id)
        reply_to = parent.user
        comment = Comment(sharer=sharer, user=user, content=content, parent=parent, reply_to=reply_to)
    else:
        comment = Comment(sharer=sharer, user=user, content=content)
    comment.save()
    return redirect(sharer)
@login_required
def xinw_comment(request,xinw_id):
    print(request.POST)
    user = request.user
    content = request.POST.get('content')
    parent_id = request.POST.get('parent')
    xinw = get_object_or_404(Xinw, id=xinw_id)
    if parent_id:
        parent = get_object_or_404(Comment, id=parent_id)
        reply_to = parent.user
        comment = Comment(xinw=xinw, user=user, content=content, parent=parent, reply_to=reply_to)
    else:
        comment = Comment(xinw=xinw, user=user, content=content)
    comment.save()
    return redirect(xinw)

"""
def sharer_comment(request, sharer_id, parent_id=None):
    sharer = get_object_or_404(Sharer, id=sharer_id)

    # 处理 POST 请求
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.sharer = sharer
            new_comment.user = request.user

            # 二级回复
            if parent_id:
                parent= Comment.objects.get(id=parent_id)
                # 若回复层级超过二级，则转换为二级
                new_parent_id = parent.get_root().id
                # 被回复人
                new_comment.reply_to = parent_comment.user
                new_comment.save()
                return HttpResponse('200 OK')

            new_comment.save()
            return redirect(sharer)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 处理 GET 请求
    elif request.method == 'POST':
        comment_form = CommentForm()
        context = {
            'comment_form': comment_form,
            'sharer_id': sharer_id,
            'parent_id': parent_id
        }
        return render(request, 'comment/commit_commit.html', context)
    # 处理其他请求
    else:
        return HttpResponse("仅接受GET/POST请求。")

@login_required
# 新增参数 parent_comment_id
def sharer_comment(request, sharer_id, parent_comment_id=None):
    sharer = get_object_or_404(Sharer, id=sharer_id)
        
    # 处理 POST 请求
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.sharer = sharer
            new_comment.user = request.user
            new_comment.save()
            return redirect(sharer)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 处理错误请求
    else:
        return HttpResponse("发表评论仅接受POST请求。")

def addComment(request):
    print(request.POST)
    user = request.user
    content = request.POST.get('content')
    parent_id = request.POST.get('parent')
    sharer = get_object_or_404(Sharer, id=request.POST.get('sharer'))
    if parent_id:
        parent = get_object_or_404(Comment, id=parent_id)
        reply_to = parent.user
        comment = Comment(sharer=sharer, user=user,content=content, parent=parent, reply_to=reply_to)
    else:
        comment = Comment(sharer=sharer, user=user, content=content)
    comment.save()
    return redirect(sharer)

"""