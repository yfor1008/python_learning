#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : alien_invasion.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/25 20:44:44
# @Docs   : 《外星人入侵》游戏, 《Python编程从入门到实践》书中的例子, 可以参考: https://github.com/ehmatthes/pcc_2e
'''

import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    """
    运行游戏
    """

    # 初始化pygame, 设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建子弹编组
    bullets = Group()

    # 游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)

        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
