#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : python_repos.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/30 14:46:37
# @Docs   : python执行web API调用
'''

import json
import requests
import socket
import socks

import pygal # 如果需要生成worldmap, 需先安装pygal_maps_world
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS # 设置style


# # 需设置代理, 否则不能连接github
# host = '127.0.0.1'
# port = 1080
# socks.setdefaultproxy(socks.SOCKS5, host, port)
# socket.socket = socks.socksocket

# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# r = requests.get(url)
# print('status code: {}'.format(r.status_code))

# response_dict = r.json()
# print(response_dict.keys())

# with open('response.json', 'w') as f:
#     json.dump(response_dict, f)

with open('response.json', 'r') as f:
    response_dict = json.load(f)

print(response_dict.keys())

# 有关仓库信息
repo_dicts = response_dict['items']

# for key in sorted(repo_dicts[0].keys()):
#     print(key)

# print('name: {}'.format(repo_dicts[0]['name']))
# print('owner: {}'.format(repo_dicts[0]['owner']['login']))
# print('stars: {}'.format(repo_dicts[0]['stargazers_count']))
# print('repository: {}'.format(repo_dicts[0]['html_url']))
# print('created: {}'.format(repo_dicts[0]['created_at']))
# print('updated: {}'.format(repo_dicts[0]['updated_at']))
# print('description: {}'.format(repo_dicts[0]['description']))


names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])
    plot_dict = {'value': repo_dict['stargazers_count'],
                 'label': repo_dict['description'] if repo_dict['description'] else '', # description为空时, pygal会报错
                 'xlink': repo_dict['html_url']} # 添加链接
    plot_dicts.append(plot_dict)

# 可视化
my_stype = RS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_stype)
chart.title = 'most starred python project on github'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
