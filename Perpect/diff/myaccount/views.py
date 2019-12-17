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
            try :
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'sign_up.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request, user)
                return redirect('grid')              # user생성시 로그인 후 메인화면으로 이동
        else:
            return render(request, 'sign_up.html', {'error':'Passwords must match'})
    else:
        return render(request, 'sign_up.html')

def login(request):

    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = auth.Authenticate(request, usernaem=username, password=password)
        if user is not None:
            auth.login(request, user)
        else :
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else: 
        return render(request, 'login.html')