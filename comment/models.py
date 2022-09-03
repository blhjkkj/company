from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from learning_logs.models import Sharer
from company.models import Xinw
from django.urls import reverse
# Create your models here.
class Comment(MPTTModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='comments',verbose_name='作者')
    content=RichTextUploadingField(verbose_name='评论内容',config_name='comment')
    created_date=models.DateTimeField(auto_now_add=True)
    sharer=models.ForeignKey(Sharer,on_delete=models.CASCADE,null=True,blank=True)
    xinw=models.ForeignKey(Xinw,on_delete=models.CASCADE,null=True,blank=True)
    parent=TreeForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='children')
    reply_to = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE, related_name='replyers')
    class Meta:
        verbose_name='评论管理'
        verbose_name_plural=verbose_name
        ordering=['created_date']
    class MPTTMeta:
        verbose_name='评论管理'
        verbose_name_plural=verbose_name
        ordering_insertion_by=['created_date']
        ordering=['-created_date']
    def __str__(self):
        return self.content
