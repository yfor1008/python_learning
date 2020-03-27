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
        初始化游戏设置
        """

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 1
        self.alien_drop_speed = 10
        self.fleet_direction = 1 # 移动方向: 1:向右移动, -1:向左移动
