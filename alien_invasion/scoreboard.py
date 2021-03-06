#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : scoreboard.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/27 14:02:46
# @Docs   : 得分相关模块
'''

import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard(object):
    """
    显示得分信息的类
    """

    def __init__(self, ai_game):
        '''
        ### Docs: 初始化得分相关的属性
        ### Args:
            - ai_game: class, AlienInvasion类的实例对象
        '''

        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # 显示得分信息的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 初始化得分, 等级, 及剩余飞船数量图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self, ):
        """
        剩余飞船数量
        """

        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_level(self, ):
        """
        将等级渲染成图像
        """

        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.settings.bg_color)

        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_score(self, ):
        """
        将得分渲染成图像
        """

        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score) # 千位分隔
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # 得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self, ):
        """
        将最高得分渲染成图像
        """

        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score) # 千位分隔
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.centerx
        # self.high_score_rect.top = self.screen_rect.top
        self.high_score_rect.top = 20

    def high_score_check(self, ):
        """
        检查是否有新的最高分
        """

        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self, ):
        """
        屏幕上显示得分
        """

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
