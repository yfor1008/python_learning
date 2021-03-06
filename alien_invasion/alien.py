#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : alien.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/27 09:08:42
# @Docs   : 外星人模块
'''

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """
    表示单个外星人的类
    """

    def __init__(self, ai_game):
        '''
        ### Docs: 初始化外星人并设置初始位置
        ### Args:
            - ai_game: class, AlienInvasion类的实例对象
        '''

        super(Alien, self).__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载外星人, 并设置rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width # 初始位置都在屏幕左上角
        self.rect.y = self.rect.height
        self.x = float(self.rect.x) # 用浮点数存储外星人位置

    def check_edges(self, ):
        """
        如果外星人位于屏幕的边缘, 返回True
        """

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self, ):
        """
        根据方向移动外星人
        """
        self.x += self.settings.alien_speed_factor * self.settings.fleet_direction
        self.rect.x = self.x

    def blitme(self, ):
        """
        在指定位置绘制外星人
        """

        self.screen.blit(self.image, self.rect)
