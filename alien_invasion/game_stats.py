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

    def __init__(self, ai_settings):
        """
        初始化统计信息
        """

        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏刚启动时处于活动状态
        self.game_active = True

    def reset_stats(self, ):
        """
        初始化在游戏期间可能变化的统计信息
        """

        self.ships_left = self.ai_settings.ship_limit
