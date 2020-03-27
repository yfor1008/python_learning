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
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, stats, ship, aliens, bullets, play_button, sb):
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, ship, aliens, bullets, play_button, sb, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, ship, aliens, bullets, play_button, sb, mouse_x, mouse_y):
    """
    响应Play按钮, 单击Play按钮时激活游戏, 重新开始游戏
    """

    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active: # 增加条件, 仅在非激活状态点击按钮才有效
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标, 游戏激活后, 不显示光标, 避免影响游戏体验
        pygame.mouse.set_visible(False)

        stats.reset_stats() # 重置游戏统计信息
        stats.game_active = True

        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        # 更新记分牌
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ship()

        # 创建一群新的外星人, 并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

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
    elif event.key == pygame.K_q:
        # 按下q键时, 退出游戏
        sys.exit()

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

def get_number_alien_x(ai_settings, alien_width):
    """
    计算每行可容纳多少外星人
    """

    available_space_x = ai_settings.screen_width - 2 * alien_width # 屏幕2边空出一个外星人宽度
    number_aliens_x = int(available_space_x / (2 * alien_width)) # 间距为外星人宽度, 所有个数=行宽/(2*alien_width)

    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """
    计算屏幕可以容纳多少行外星人
    """

    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height # 飞船上方留出空白
    number_rows = int(available_space_y / (2 * alien_height)) # 间距为外星人高度, 行数=高/(2*alien_height)

    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """
    创建一个外星人, 并放在相应位置
    """

    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """
    创建外星人群:
    创建一个外星人, 计算每一行可容纳多少个外星人
    外星人间距为外星人宽度
    """

    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button, sb):
    """
    更新屏幕上的图像, 并切换到新屏幕
    """

    # 重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)

    # 在飞船和外星人后重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 显示得分
    sb.show_score()

    # 如果游戏处于非激活状态, 则绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, ship, aliens, bullets, sb):
    """
    更新子弹位置, 并删除已消失的子弹
    检查是否击中外星人, 如果击中则删除应用的子弹和外星人
    """

    bullets.update()

    # 删除已消失(屏幕之外)的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    # print(len(bullets))

    check_bullet_alien_collisions(ai_settings, screen, stats, ship, aliens, bullets, sb)

def check_bullet_alien_collisions(ai_settings, screen, stats, ship, aliens, bullets, sb):
    """
    检测子弹和外星人之间的碰撞, 删除发生碰撞的子弹和外星人
    """

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        # 如果击中外星人, 则更新得分和记分牌
        for alien in collisions.values():
            stats.score += ai_settings.alien_points * len(alien)
            sb.prep_score()
        high_score_check(stats, sb)

    # 如果外星人为空, 删除所有子弹并创建新的外星人群
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed() # 加快游戏节奏
        create_fleet(ai_settings, screen, ship, aliens)

        # 外星人群被消灭, 提高一个等级, 更新等级及记分牌
        stats.level += 1
        sb.prep_level()

def check_fleet_edges(ai_settings, aliens):
    """
    有外星人达到屏幕边缘时, 采取相应措施
    """
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """
    外星人群整体下移, 并改变移动方向
    """

    for alien in aliens:
        alien.rect.y += ai_settings.alien_drop_speed
    ai_settings.fleet_direction *= -1

def updata_aliens(ai_settings, screen, stats, ship, aliens, bullets, sb):
    """
    检查是否有外星人位于屏幕边缘, 并更新外星人群中所有外星人的位置
    """

    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        # print("Ship hit!!!")
        ship_hit(ai_settings, screen, stats, ship, aliens, bullets, sb)
    
    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, screen, stats, ship, aliens, bullets, sb)

def ship_hit(ai_settings, screen, stats, ship, aliens, bullets, sb):
    """
    响应飞船被撞, 飞船剩余数量-1
    """

    if stats.ships_left > 0:
        stats.ships_left -= 1

        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人, 并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 更新记分牌
        sb.prep_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True) # 游戏处于非激活状态时, 显示光标

def check_aliens_bottom(ai_settings, screen, stats, ship, aliens, bullets, sb):
    """
    检查是否有外星人到达屏幕底端
    """

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 只要有外星人到达屏幕底端, 则像飞船被撞一样处理
            ship_hit(ai_settings, screen, stats, ship, aliens, bullets, sb)
            break

def high_score_check(stats, sb):
    """
    检查是否有新的最高分
    """

    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
