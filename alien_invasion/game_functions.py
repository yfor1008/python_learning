#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : game_functions.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/26 20:39:54
# @Docs   : 游戏运行相关的函数
'''

import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """
    响应键盘和鼠标事件
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """
    响应按键
    """
    if event.key == pygame.K_RIGHT:
        # 按下向右方向键时, 右移标志为True
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 按下向左方向键时, 左移标志为True
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 按下空格键时, 创建一颗子弹并将其放入bullets中
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """
    响应松开
    """
    if event.key == pygame.K_RIGHT:
        # 松开向右方向键时, 右移标志为False
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 松开向左方向键时, 左移标志为False
        ship.moving_left = False

def fire_bullet(ai_settings, screen, ship, bullets):
    """
    没有达到限制, 就发射一颗子弹
    """

    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(ai_settings, screen, ship, bullets):
    """
    更新屏幕上的图像, 并切换到新屏幕
    """

    # 重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 在飞船和外星人后重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    """
    更新子弹位置, 并删除已消失的子弹
    """

    bullets.update()

    # 删除已消失(屏幕之外)的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    print(len(bullets))
