#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : urls.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/31 15:18:20
# @Docs   : 定义URL模式
'''

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # 登录界面
    path('', include('django.contrib.auth.urls')),
    # 注销
    path('logout/', views.logout_view, name='logout'),
    # 注册页面
    path('register/', views.register, name='register')
]
