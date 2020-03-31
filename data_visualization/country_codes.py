#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : country_codes.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/30 13:52:13
# @Docs   : 根据国家名获取国别码
'''

# from pygal.i18n import COUNTRIES # pygal2.0.0版本已移除i18n模块, 需要安装pygal-maps-world, 然后使用下面方式
# from pygal.maps.world import COUNTRIES # 方式1
from pygal_maps_world.i18n import COUNTRIES # 方式2

def get_country_code(country_name):
    '''
    ### Docs: pygal使用2个字母的国别码, 需根据国家名查找国别码
    ### Args:
        - country_name: str, 国家名
    ### Returns:
        - 2个字母的国别码
    '''

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

if __name__ == "__main__":

    print(get_country_code('Andorra'))
    print(get_country_code('United Arab Emirates'))
    print(get_country_code('China'))
