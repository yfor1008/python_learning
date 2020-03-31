#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : highs_lows.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/29 17:29:49
# @Docs   : 读取csv文件, 分析天气数据
'''

import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'

dates, highs, lows = [], [], []
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # for index, col_header in enumerate(header_row):
    #     print(index, col_header)

    # for row in reader:
    #     dates.append(datetime.strptime(row[0], '%Y-%m-%d')) # strptime将字符串解析成时间格式, strftime将时间格式格式化成字符串
    #     highs.append(int(row[1]))
    #     lows.append(int(row[3]))

    for row in reader:
        try:
            cur_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(cur_date, 'missing data')
        else:
            # 数据有问题时, 取前面的数据填充
            dates.append(cur_date)
            highs.append(high)
            lows.append(low)

# 绘制图像
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='r')
plt.plot(dates, lows, c='b')

# 设置格式
plt.title('High temperature', fontsize=24)
plt.xlabel('', fontsize=14)
plt.ylabel('temperature(F)', fontsize=14)
# plt.axis([0, 1100, 0, 1100000])
# plt.tick_params(axis='both', labelsize=14)
# plt.axis('off')

plt.fill_between(dates, highs, lows, facecolor='b', alpha=0.3) # 填充中间数

fig.autofmt_xdate() # 自动设置格式, 避免重叠

plt.show()
