#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : alien_invasion.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/25 20:44:44
# @Docs   : 《外星人入侵》游戏, 《Python编程从入门到实践》书中的例子, 可以参考: https://github.com/ehmatthes/pcc
'''

import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from ship import Ship
from pygame.sprite import Group

class AlienInvasion(object):
    """游戏管理的类"""

    def __init__(self, ):
        """
        初始化游戏, 创建游戏资源
        """

        # 初始化pygame, 设置和屏幕对象
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # 统计信息及记分牌
        self.stats = GameStats(self)
        self.sb = ScoreBoard(self)

        # 飞船
        self.ship = Ship(self)
        # 子弹编组
        self.bullets = Group()
        # 外星人群
        self.aliens = Group()
        self.create_fleet()

        # Play按钮
        self.play_button = Button(self, "Play")

    def run_game(self, ):
        """
        运行游戏
        """

        while True:
            # 监视键盘和鼠标事件
            self.check_events()

            if self.stats.game_active:
                # 游戏处于激活状态时, 才更新
                self.ship.update()
                self.update_bullets()
                self.updata_aliens()

            # 更新屏幕
            self.update_screen()

    def check_events(self, ):
        """
        响应键盘和鼠标事件
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

    def check_keydown_events(self, event):
        """
        响应按键
        """
        if event.key == pygame.K_RIGHT:
            # 按下向右方向键时, 右移标志为True
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # 按下向左方向键时, 左移标志为True
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            # 按下空格键时, 创建一颗子弹并将其放入bullets中
            self.fire_bullet()
        elif event.key == pygame.K_q:
            # 按下q键时, 退出游戏
            sys.exit()

    def check_keyup_events(self, event):
        """
        响应松开
        """
        if event.key == pygame.K_RIGHT:
            # 松开向右方向键时, 右移标志为False
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # 松开向左方向键时, 左移标志为False
            self.ship.moving_left = False

    def check_play_button(self, mouse_pos):
        """
        响应Play按钮, 单击Play按钮时激活游戏, 重新开始游戏
        """

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active: # 仅在非激活状态点击按钮才有效
            # 重置游戏设置
            self.settings.initialize_dynamic_settings()

            # 隐藏光标, 游戏激活后, 不显示光标, 避免影响游戏体验
            pygame.mouse.set_visible(False)

            self.stats.reset_stats() # 重置游戏统计信息
            self.stats.game_active = True

            # 清空外星人和子弹列表
            self.aliens.empty()
            self.bullets.empty()

            # 更新记分牌
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # 创建一群新的外星人, 并将飞船放到屏幕底端中央
            self.create_fleet()
            self.ship.center_ship()

    def fire_bullet(self, ):
        """
        没有达到限制, 就发射一颗子弹
        """

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def create_fleet(self, ):
        """
        创建外星人群:
        创建一个外星人, 计算每一行可容纳多少个外星人
        外星人间距为外星人宽度
        """

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - 2 * alien_width # 屏幕2边空出一个外星人宽度
        number_aliens_x = int(available_space_x / (2 * alien_width)) # 间距为外星人宽度, 所有个数=行宽/(2*alien_width)s

        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - 3 * alien_height - ship_height # 飞船上方留出空白
        number_rows = int(available_space_y / (2 * alien_height)) # 间距为外星人高度, 行数=高/(2*alien_height)

        # 创建外星人群
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.create_alien(alien_number, row_number)

    def create_alien(self, alien_number, row_number):
        """
        创建一个外星人, 并放在相应位置
        """

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def update_bullets(self, ):
        """
        更新子弹位置, 并删除已消失的子弹
        检查是否击中外星人, 如果击中则删除应用的子弹和外星人
        """

        self.bullets.update()

        # 删除已消失(屏幕之外)的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)

        self.check_bullet_alien_collisions()

    def check_bullet_alien_collisions(self, ):
        """
        检测子弹和外星人之间的碰撞, 删除发生碰撞的子弹和外星人
        """

        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            # 如果击中外星人, 则更新得分和记分牌
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.high_score_check()

        # 如果外星人为空, 删除所有子弹并创建新的外星人群
        if len(self.aliens) == 0:
            self.bullets.empty()
            self.settings.increase_speed() # 加快游戏节奏
            self.create_fleet()

            # 外星人群被消灭, 提高一个等级, 更新等级及记分牌
            self.stats.level += 1
            self.sb.prep_level()

    def updata_aliens(self, ):
        """
        检查是否有外星人位于屏幕边缘, 并更新外星人群中所有外星人的位置
        """

        self.check_fleet_edges()
        self.aliens.update()

        # 检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()
        
        # 检查是否有外星人到达屏幕底端
        self.check_aliens_bottom()

    def check_fleet_edges(self, ):
        """
        有外星人达到屏幕边缘时, 采取相应措施
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self, ):
        """
        外星人群整体下移, 并改变移动方向
        """

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.fleet_direction *= -1

    def ship_hit(self, ):
        """
        响应飞船被撞, 飞船剩余数量-1
        """

        self.stats.ships_left -= 1
        if self.stats.ships_left > 0:
            # self.stats.ships_left -= 1 # 此条件需放到比较之前, 当ships_left=1时, 该分支仍会执行, 但此时的飞船数已为0, 不应该继续执行

            # 清空外星人和子弹列表
            self.aliens.empty()
            self.bullets.empty()

            # 创建一群新的外星人, 并将飞船放到屏幕底端中央
            self.create_fleet()
            self.ship.center_ship()

            # 暂停
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True) # 游戏处于非激活状态时, 显示光标

        # 更新记分牌
        self.sb.prep_ships()

    def check_aliens_bottom(self, ):
        """
        检查是否有外星人到达屏幕底端
        """

        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 只要有外星人到达屏幕底端, 则像飞船被撞一样处理
                self.ship_hit()
                break

    def update_screen(self, ):
        """
        更新屏幕上的图像, 并切换到新屏幕
        """

        # 重新绘制屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # 在飞船和外星人后重绘所有子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 显示得分
        self.sb.show_score()

        # 如果游戏处于非激活状态, 则绘制Play按钮
        if not self.stats.game_active:
            self.play_button.draw_button()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

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

    # 创建外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个用于存储游戏统计信息的对象实例, 并创建记分牌
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, ship, aliens, bullets, play_button, sb)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, ship, aliens, bullets, sb)
            gf.updata_aliens(ai_settings, screen, stats, ship, aliens, bullets, sb)

        # 更新屏幕
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button, sb)


# run_game()
if __name__ == "__main__":
    
    # run_game()
    ai = AlienInvasion()
    ai.run_game()
