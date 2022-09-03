from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
#ckeditor相关设置
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.
class Topic(models.Model):#母表
    caption=models.CharField(max_length=30,verbose_name='主题')
    desc=models.TextField(max_length=200,blank=True,null=True,verbose_name='分类描述')
    date_added=models.DateTimeField(auto_now_add=True,blank=True,null=True,verbose_name='日期')
    tags=models.ImageField(blank=True,null=True,verbose_name='图片')
    class Meta:
        verbose_name = '分类'
        verbose_name_plural ='资讯分类'
    def get_xinws(self):
        #解决一个页面显示所有分类及分类下按时间逆排序问题
        return Xinw.objects.filter(topic=self).order_by('-date_added')[:3]
    
    def __str__(self):
        """返回模型的字符串表示"""
        return (self.caption)
    
    
class Xinw(models.Model):#子表
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE,verbose_name='主题')
    caption=models.TextField(max_length=200,verbose_name='资讯标题')
    author=models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='作者')
    date_added = models.DateTimeField(auto_now_add=True,verbose_name='日期')
    origin=models.CharField(max_length=100,blank=True,null=True,verbose_name='来源')
    content=RichTextUploadingField(verbose_name='资讯内容')       
    class Meta:
        verbose_name='资讯'
        verbose_name_plural='所有资讯'
    def get_absolute_url(self):
        return reverse('company:datil',args=[self.id])#获取文章网址
    
    def __str__(self):
        if len(self.content)>30:
            return f"{(self.caption,self.content[:30])}..."

        else:
            return f'{self.caption,self.content}'
class Video(models.Model):
    video=models.FileField(verbose_name='视频')
    topic=models.CharField(max_length=100,verbose_name='标题')
    class Meta:
        verbose_name='所有视频'
        verbose_name_plural=verbose_name
        def __str__ (self):
            return self.video
"""
class Post(models.Model):
    content = RichTextUploadingField()
#评论模型
class Comment(models.Model):
    name = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    text = RichTextUploadingField()
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='评论')
    pre_comment = models.ForeignKey('self',on_delete=models.DO_NOTHING,blank=True,null=True,verbose_name='父评论id') 
    xinw = models.ForeignKey(Xinw,on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name='评论'
        verbose_name_plural='评论'
 
    def __str__(self):
        if len(self.text):
            return f"{str(self.text[:50])}..."
        else:
            return f"{str(self.text)}"

"""
#公司介绍模板
class About(models.Model):
    text=RichTextUploadingField(verbose_name='公司介绍')
    linkman=models.CharField(max_length=10,blank=True,null=True,verbose_name='联系人')
    phone=models.IntegerField(verbose_name='联系电话')
    MP=models.IntegerField(verbose_name='联系人手机号')
    class Meta:
        verbose_name='公司介绍'
        verbose_name_plural='公司介绍'
    def __str__(self):
        if len(self.text):
            return f"{str(self.text[:50])}..."
        else:
            return f"{str(self.text)}"

    

