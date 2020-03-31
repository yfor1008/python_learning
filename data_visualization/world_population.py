#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : world_population.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2020/03/30 12:12:42
# @Docs   : 显示人口数量
'''

import json
import pygal
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
from country_codes import get_country_code

filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f) # load针对文件, loads针对内存

cc_populations = {}
# 输出人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        # print('{}: {}'.format(country_name, population))
        if code:
            # print('{}: {}'.format(code, population))
            cc_populations[code] = population
        else:
            # 并非所有的人口数量对应的都是国家, 有些人口数量对应的时地区(阿拉伯世界)和经济类群
            print('ERROE - {}'.format(country_name))

# 根据人口数量将所有国家分成3组
cc_pop1, cc_pop2, cc_pop3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 1000000:
        cc_pop1[cc] = pop
    elif pop < 1000000000:
        cc_pop2[cc] = pop
    else:
        cc_pop3[cc] = pop

# wm = pygal.Worldmap() # 需安装pygal_maps_world, 然后用pygal.maps.world.World()代替
wm_stype = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_stype)
# wm.title = 'North, Central, and South America'
# wm.add('North America', ['ca', 'mx', 'us'])
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])
# wm.render_to_file('americas.svg')
# wm.title = "World Populations in 2010, by country"
# wm.add('2010', cc_populations)
# wm.render_to_file('world_populations.svg')
wm.title = "World Populations in 2010, by country"
wm.add('0-10m', cc_pop1)
wm.add('10m-1bn', cc_pop2)
wm.add('>1bn', cc_pop3)
wm.render_to_file('world_populations.svg')
