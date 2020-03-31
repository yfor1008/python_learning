#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : urls.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/31 10:22:25
# @Docs   : 定义URL模式
'''

from django.urls import path
from . import views

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 所有主题
    path('topics/', views.topics, name='topics'),
    # 特定主题的详细页面
    path('topics/<int:topic_id>', views.topic, name='topic'),
    # 添加新主题的页面
    path('new_topic/', views.new_topic, name='new_topic'),
    # 添加新条目的页面
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    # 用于编辑条目的页面
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]
