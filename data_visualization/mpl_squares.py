#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : mpl_squares.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/27 20:30:41
# @Docs   : 绘制平方数折线图
'''

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth=3)

# 设置图标标题, 并坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14) # axis : ['x' | 'y' | 'both'], 设置坐标轴刻度

plt.show()
