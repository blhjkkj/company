from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
"""
class Questionnaire(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False,verbose_name='创建时间')
    modified_at = models.DateTimeField(auto_now=True, editable=False,verbose_name='修改时间')
    is_active = models.BooleanField(default=True,verbose_name='是否发布')
    participants = models.ManyToManyField(User,related_name='questonnaires')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,)   
    def __str__(self):
        return f"{(self.user, '的问卷')}"  
    class Meta:
        verbose_name='调查问卷'
        verbose_name_plural=verbose_name

        ordering = ["-created_at"]
"""
class Question(models.Model):
    TYPE=[
    (0,'单选题'),
    (1,'多选题'),
    (2,'问答题'),
    (3,'上传文件')

    ]
    question = models.CharField(max_length=200, verbose_name="问题")
    question_type=models.IntegerField(choices=TYPE,verbose_name='问题类型')
    required = models.BooleanField(default=True, help_text="这个问题是否必须回答")
    #questionnaire = models.ForeignKey(Questionnaire,on_delete=models.DO_NOTHING)

    order_in_list = models.IntegerField(default=1)  # 在问卷列表中的顺序，从1开始

    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:

        abstract = True
"""
class ChoiceQuestion(Question):
    #选择题
    multi_choice = models.BooleanField(default=False, verbose_name="是否为多选")
class Choice(models.Model):
    question = models.ForeignKey(ChoiceQuestion, on_delete= models.CASCADE,related_name="choices")

    description = models.CharField(max_length=50,verbose_name='说明')

    multi_choice = models.BooleanField(default=False, verbose_name="是否为多选")

    order_in_list = models.IntegerField(default=1)  # 在选项列表中的顺序，从1开始
class NonChoiceQuestion(Question):
    STYPE=[
    (0,'问答题'),
    (1,'上传文件')
    ]

    type = models.SmallIntegerField(verbose_name="主观题类型",

    choices=STYPE, default=0)
    """


"""

class AnswerSheet(models.Model):

    #答卷的抽象

    user = models.ForeignKey(settings.AUTH_USER_MODEL,models.DO_NOTHING,verbose_name='填表人')      # 答题者

    questionnaire = models.ForeignKey(Questionnaire,on_delete=models.CASCADE)     # 对应问卷

    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    modified_at = models.DateTimeField(auto_now=True, editable=False)

    is_active = models.BooleanField(default=True)

class Answer(models.Model):

    #答案的基类

    answer_sheet = models.ForeignKey(AnswerSheet,on_delete=models.DO_NOTHING)    
    class Meta:

        abstract = True
class SingleChoiceAnswer(Answer):
    #单选题的答案

    choice = models.ForeignKey(Choice,on_delete=models.DO_NOTHING, related_name="single_choice_answers")#单选题
    question = models.ForeignKey(ChoiceQuestion, on_delete=models.DO_NOTHING,related_name="single_choice_answer_set")
class MultiChoiceAnswer(Answer):

    #多选题的答案

    choices = models.ManyToManyField(Choice, related_name="multi_choice_answers")

    question = models.ForeignKey(ChoiceQuestion, on_delete=models.DO_NOTHING,related_name="multi_choice_answers")
class TextAnswer(Answer):

    #文字题的答案

    text = models.TextField()

    question = models.ForeignKey(NonChoiceQuestion,on_delete=models.DO_NOTHING)
class FileAnswer(Answer):

    file = models.ImageField(upload_to="uplod/questions")

    question = models.ForeignKey(NonChoiceQuestion,on_delete=models.DO_NOTHING)

    is_image = models.BooleanField(default=True)
"""

