from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def sign_up(request):

    return render(request, 'sign_up.html')

def login(request):

    return render(request, 'login.html')