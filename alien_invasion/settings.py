#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : settings.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/26 20:08:15
# @Docs   : 设置模块
'''

class Settings(object):
    """
    存储所有设置的类
    """

    def __init__(self, ):
        """
        初始化游戏静态设置
        """

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 30

        # 外星人设置
        self.alien_drop_speed = 20

        # 提高游戏速度
        self.speed_scale = 1.1
        # 提高外星人得分点数
        self.score_scale = 1.5

        # 动态设置
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self, ):
        """
        初始化随游戏进行而变化的设置
        """

        # 飞船设置
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 3

        # 外星人设置
        self.alien_speed_factor = 1
        self.alien_points = 50 # 分数
        self.fleet_direction = 1 # 移动方向: 1:向右移动, -1:向左移动

    def increase_speed(self, ):
        """
        提高速度设置
        """

        self.ship_speed_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale

        self.alien_points = int(self.alien_points * self.score_scale)
