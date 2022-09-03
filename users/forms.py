from django import forms
class ResetPasswordForm(forms.Form):
    """
    重置密码表单，需要手机号验证
    """

    tel = forms.CharField(max_length=20, required=True, label='Telephone')

    # 获取电话号码
    def clean_identity_tel(self):
        tel = self.cleaned_data['tel']
        print(tel)
        """
        由于用get获取对象，如果获取不到会报错，所以这里使用filter
        获取失败返回空对象列表
        在UserProfile中筛选符合条件的用户，返回用户名
        """
        username = UserProfile.objects.filter(tel=tel)
        if not username:
            raise forms.ValidationError("手机号错误!!")

        return self.cleaned_data['tel']

    def save(self, request, **kwargs):
        return self.cleaned_data['tel']