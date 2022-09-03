from django import forms
from ckeditor_uploader.fields import RichTextUploadingFormField
from .models import Topic,Sharer

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

class SharerForm(forms.ModelForm):
    class Meta:
        model=Sharer
        fields=['capt','content','action']
        labels={'content':''}
        widgets={'content':forms.Textarea(attrs={'cols':80})}