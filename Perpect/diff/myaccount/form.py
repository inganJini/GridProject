from django import forms
from django.contrib.auth.forms import UserCreationForm  # 장고에서 기본적으로 제공하는 form
from django.contrib.auth.models import User

class MyUserForm(UserCreationForm):
    #email = forms.EmailField(required=True) # 이메일 필드 추가

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def save(self, commit=True):  # 저장하는 부분 오버라이딩
        user = super(CreateUserForm, self).save(commit=False) # 본인의 부모를 호출해서 저장하겠다
        
        user.email = self.cleaned_data["email"]
        if commit:  
            user.save()
        return user