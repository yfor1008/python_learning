from django.shortcuts import render, redirect, Http404
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicFrom, EntryFrom

# Create your views here.
def index(request):
    '''学习笔记主页'''
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    '''显示所有主题'''
    # topics = Topic.objects.order_by('date_added')
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    '''显示单个主题及其所有条目'''
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise 
    entries = topic.entry_set.order_by('date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    '''添加新主题'''
    if request.method != 'POST':
        # 没有数据, 提交空表单
        form = TopicFrom()
    else:
        # POST提交数据, 对数据进行处理
        form = TopicFrom(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    '''在特定主题中添加新条目'''
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 没有数据, 提交空表单
        form = EntryFrom()
    else:
        # POST提交数据, 对数据进行处理
        form = EntryFrom(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    '''编辑已有条目'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求, 使用当前条目填充表单
        form = EntryFrom(instance=entry)
    else:
        # POST提交数据, 对数据进行处理
        form = EntryFrom(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic,  'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)

