#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : bullet.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/26 21:18:08
# @Docs   : 子弹模块
'''

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    飞船发射子弹管理的类
    """

    def __init__(self, ai_settings, screen, ship):
        """
        在飞船所处位置创建一个子弹对象实例
        """

        super(Bullet, self).__init__()
        self.screen = screen

        # 设置子弹位置, 飞船正上方
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y) # 用浮点数存储子弹位置
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self, ):
        """
        向上移动子弹
        """

        self.y -= self.speed_factor # pygame中原点在左上角, 向右下方移动时, 坐标值增大
        self.rect.y = self.y
    
    def draw_bullet(self, ):
        """
        屏幕上绘制子弹
        """

        pygame.draw.rect(self.screen, self.color, self.rect)
