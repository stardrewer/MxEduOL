# coding:utf8
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend  # 自定义逻辑
from django.db.models import Q  # 并集查询
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile
from .forms import LoginForm, RegisterForm
from utils.email_send import send_register_email


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):  # 实际上就是变了一种代码的组织形式，和下面的user_login是一样的

    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)  # 传参为字典 -> post
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)  # 为什么改了半天不显示errorput呢，就是因为把request.POST扔到了上面的get
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            pass_word = request.POST.get('password', '')  # 取出username和password

            user_profile = UserProfile()  # 数据库实例化
            user_profile.username = user_name  # 传值给数据库
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)  # 密码加密后再存储
            user_profile.save()

            send_register_email(user_name, 'register')
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})