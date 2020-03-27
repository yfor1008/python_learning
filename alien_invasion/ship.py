#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : ship.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/26 20:18:06
# @Docs   : 飞船模块
'''

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """
    飞船模块
    """

    def __init__(self, ai_game):
        '''
        ### Docs: 初始化飞船并设置初始位置
        ### Args:
            - ai_game: class, AlienInvasion类的实例对象
        '''
        super(Ship, self).__init__()

        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 飞船属性
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self, ):
        """
        在指定位置绘制飞船
        """
        self.screen.blit(self.image, self.rect)

    def update(self, ):
        """
        根据移动标志调整飞船位置
        """

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        self.rect.centerx = self.center

    def center_ship(self, ):
        """
        让飞船在屏幕中央
        """

        self.center = self.screen_rect.centerx
