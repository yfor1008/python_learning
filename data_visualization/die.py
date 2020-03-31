#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : die.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/29 13:16:49
# @Docs   : 骰子类
'''

from random import randint

class Die(object):
    """骰子类"""

    def __init__(self, num_sides=6):
        '''
        ### Docs: 骰子默认为6面
        '''

        self.num_sides = num_sides
    
    def roll(self, ):
        '''
        ### Docs: 掷骰子, 返回一个[1, num_sides]之间的随机数
        '''

        return randint(1, self.num_sides)

if __name__ == "__main__":

    import pygal

    die_1 = Die()
    die_2 = Die()

    # 掷几次筛子
    results_1 = []
    for roll_num in range(1000):
        result = die_1.roll()
        results_1.append(result)
    results_2 = []
    for roll_num in range(1000):
        result = die_2.roll()
        results_2.append(result)

    # 统计结果
    frequencies_1 = [results_1.count(value) for value in range(1, die_1.num_sides+1)]
    frequencies_2 = [results_2.count(value) for value in range(1, die_2.num_sides+1)]

    # 可视化
    hist = pygal.Bar()
    hist.title = "Results of rolling D6 {} times".format(1000)
    hist.x_labels = [str(value) for value in range(1, die_1.num_sides+1)]
    hist.x_title = "Value"
    hist_y_title = "Frequency"

    hist.add('D6-1', frequencies_1)
    hist.add('D6-2', frequencies_2)
    hist.render_to_file('D6.svg')
