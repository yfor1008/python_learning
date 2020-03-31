#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : scatter_squares.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/29 10:24:09
# @Docs   : 绘制散点图
'''

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, s=40, c='r', edgecolors='g') # s为点的大小, c为点颜色, edgecolors为点边缘颜色
plt.scatter(x_values, y_values, s=40, c=y_values, cmap=plt.cm.Blues, edgecolors='none') # cmap为点颜色c的映射方式

# 设置图标标题, 并坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置坐标轴范围
plt.axis([0, 1100, 0, 1100000])

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14) # axis : ['x' | 'y' | 'both'], 设置坐标轴刻度

# 保存图像
plt.savefig('squares_plot.png', bbox_inches='tight') # bbox_inches='tight'会去除图像多余空白

plt.show()
