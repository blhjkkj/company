from django import forms
from ckeditor_uploader.fields import RichTextUploadingFormField
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']
        labels={'content':''}
        widgets={'content':forms.Textarea(attrs={'cols':80})}