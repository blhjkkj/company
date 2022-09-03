from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.timezone import timezone
from django.urls import reverse
# Create your models here.

class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField( max_length=200,verbose_name='类别')
    date_added = models.DateTimeField(auto_now_add=True,verbose_name='日期')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = '主题'
        verbose_name_plural ='分类主题'
    def get_sharers(self):
        #解决一个页面显示所有分类及分类下按时间逆排序问题
        return Sharer.objects.filter(topic=self).order_by('-date_added')[:4]

    def __str__(self):
        """返回模型的字符串表示。"""
        return self.text

class Sharer(models.Model):
    """学到的某个主题的具体知识"""
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='entries',verbose_name='作者')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,verbose_name='主题')
    capt=models.CharField(max_length=100,verbose_name='标题')
    date_added = models.DateTimeField(auto_now_add=True,verbose_name='日期')
    content = RichTextUploadingField(verbose_name='内容')
    action=models.BooleanField(default=False,verbose_name='设为私有')
    
    class Meta:
        verbose_name = '笔记'
        verbose_name_plural ='我的笔记'
    def get_absolute_url(self):
        return reverse('learning_logs:阅读全文',args=[self.id])#获取文章网址
    def __str__(self):
        """返回模型的字符串表示。"""
        return self.capt
"""
# django-mptt

# 替换 models.Model 为 MPTTModel
class Comment(MPTTModel):
    content=RichTextUploadingField(config_name='comment',verbose_name='内容')

    # 新增，mptt树形结构
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    # 新增，记录二级评论回复给谁, str
    reply_to = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replyers'
    )

    # 替换 Meta 为 MPTTMeta
    # class Meta:
    #     ordering = ('created',)
    class MPTTMeta:
        order_insertion_by = ['created']
"""