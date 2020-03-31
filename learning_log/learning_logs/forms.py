#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : forms.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/31 12:53:18
# @Docs   : 添加表单
'''

from django import forms
from .models import Topic, Entry

class TopicFrom(forms.ModelForm):
    '''添加新主题的网页'''
    class Meta(object):
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryFrom(forms.ModelForm):
    '''添加具体条目的网页'''
    class Meta(object):
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

