from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # 장고에서 기본적으로 제공하는 form
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Create your views here.


def sign_up(request):
    # 계정생성 전 중복 체크 필요함!!
    if request.method == 'POST' :
        if request.POST['password1'] == request.POST['password2'] :
            user = User.object.create_user(request.POST['username'],request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'sign_up.html')

def login(request):

    #if request.method == 'POST' :
    #    username = request.POST['username']
    #    password = request.POST['password']
    #    user = user.Authenticate(request, usernaem=username, password=password)
        

    return render(request, 'login.html')