#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : game_stats.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/27 11:23:24
# @Docs   : 游戏信息统计模块
'''

class GameStats(object):
    """
    游戏统计信息
    """

    def __init__(self, ai_game):
        '''
        ### Docs: 初始化统计信息
        ### Args:
            - ai_game: class, AlienInvasion类的实例对象
        '''

        self.settings = ai_game.settings
        self.reset_stats()

        # 游戏刚启动时处于活动状态
        self.game_active = False

        # 最高得分, 任何情况下都不应重置最高得分
        self.high_score = 0

    def reset_stats(self, ):
        """
        初始化在游戏期间可能变化的统计信息
        """

        self.ships_left = self.settings.ship_limit
        self.score = 0 # 得分
        self.level = 1 # 等级
