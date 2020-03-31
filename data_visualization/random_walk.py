#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : random_walk.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/29 10:47:34
# @Docs   : 随机漫步
'''

from random import choice

class RandomWalk(object):
    """生成随机漫步数据的类"""

    def __init__(self, num_points=10000):
        '''
        ### Docs: 初始化相关属性
        ### Args:
            - num_points: int, 点的个数
        '''

        self.num_points = num_points

        # 所有点的位置, 初始设置在原点(0, 0)
        self.x_values = [0] * self.num_points
        self.y_values = [0] * self.num_points

        # 当前点index
        self.cnt_point = 0

        # 方向及位移
        self.direction = [-1, 1] # 分别表示后退和前进
        self.distance = [0, 1, 2, 3, 4] # 可能移动的距离

    def fill_walk(self, ):
        '''
        ### Docs: 计算所有的点
        '''

        while self.cnt_point < self.num_points - 1:
            x_direction = choice(self.direction)
            x_distance = choice(self.distance)
            x_step = x_direction * x_distance
            y_direction = choice(self.direction)
            y_distance = choice(self.distance)
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            else:
                # 更新计数
                self.cnt_point += 1
                # 在前一个点的基础上计算当前点
                # print(self.cnt_point)
                cur_x = self.x_values[self.cnt_point - 1] + x_step
                cur_y = self.y_values[self.cnt_point - 1] + y_step

                self.x_values[self.cnt_point] = cur_x
                self.y_values[self.cnt_point] = cur_y

if __name__ == "__main__":
    
    import matplotlib.pyplot as plt

    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置颜色
    plt.scatter(rw.x_values, rw.y_values, s=1, c=range(rw.num_points), cmap=plt.cm.Blues)

    # 突出起点和终点
    plt.scatter(0, 0, c='g', s= 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='r', s=100)

    # 隐藏坐标轴
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    plt.axis('off')

    plt.show()

