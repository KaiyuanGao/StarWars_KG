# coding=utf-8
# @author: kaiyuan
# blog: https://blog.csdn.net/Kaiyuan_sjtu
# coding:utf8
"""
建立知识图谱中的节点node和链接link信息
"""

import json


##################################################
# 第一部分 读取数据
##################################################

# 字典定义六类实体
films = {}
characters = {}
planets = {}
starships = {}
vehicles = {}
species = {}

# 读取电影链接
fr = open('data/films.csv', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    films[tmp['url']] = tmp
    print(tmp['url'], tmp)
fr.close()

# 读取人物数据
fr = open('data/characters.csv', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    characters[tmp['url']] = tmp
fr.close()

# 读取星球数据
fr = open('data/planets.csv', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    planets[tmp['url']] = tmp
fr.close()

# 读取飞船数据
fr = open('data/starships.csv', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    starships[tmp['url']] = tmp
fr.close()

# 读取装备数据
fr = open('data/vehicles.csv', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    vehicles[tmp['url']] = tmp
fr.close()

# 读取物种数据
fr = open('data/species.csv', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    species[tmp['url']] = tmp
fr.close()


##################################################
# 第二部分 获取节点和边
##################################################

#定义节点和边
nodes = []
links = []

# nodes实体包括id(电影名称)、class、group、size
# links为电影与人物、星球、种族、装备、飞船的边
for key, value in films.items():
    nodes.append({'id': value['title'], 'class': 'film', 'group': 0, 'size': 20})

    # 遍历value['characters'] 如果存在则建立一条电影到人物的边, 边的权重设置为3
    # characters 人物
    for item in value['characters']:
        if item in characters:
            links.append({'source': value['title'], 'target': characters[item]['name'], 'value': 3})

    # planets 星球
    for item in value['planets']:
        if item in planets:
            links.append({'source': value['title'], 'target': planets[item]['name'], 'value': 3})

    # species 种族
    for item in value['species']:
        if item in species:
            links.append({'source': value['title'], 'target': species[item]['name'], 'value': 3})

    # starships
    for item in value['starships']:
        if item in starships:
            links.append({'source': value['title'], 'target': starships[item]['name'], 'value': 3})

    # vehicles
    for item in value['vehicles']:
        if item in vehicles:
            links.append({'source': value['title'], 'target': vehicles[item]['name'], 'value': 3})

# 建立人物的节点和关联
for key, value in characters.items():
    nodes.append({'id': value['name'], 'class': 'character', 'group': 1, 'size': 5})

    # films
    for item in value['films']:
        if item in films:
            links.append({'source': value['name'], 'target': films[item]['title'], 'value': 3})

    # planets
    if value['homeworld'] in planets:
        links.append({'source': value['name'], 'target': planets[value['homeworld']]['name'], 'value': 3})

    # species
    for item in value['species']:
        if item in species:
            links.append({'source': value['name'], 'target': species[item]['name'], 'value': 3})

    # starships
    for item in value['starships']:
        if item in starships:
            links.append({'source': value['name'], 'target': starships[item]['name'], 'value': 3})

    # vehicles
    for item in value['vehicles']:
        if item in vehicles:
            links.append({'source': value['name'], 'target': vehicles[item]['name'], 'value': 3})

for key, value in planets.items():
    nodes.append({'id': value['name'], 'class': 'planet', 'group': 2, 'size': 16})

    # films
    for item in value['films']:
        if item in films:
            links.append({'source': value['name'], 'target': films[item]['title'], 'value': 3})

    # characters
    for item in value['residents']:
        if item in characters:
            links.append({'source': value['name'], 'target': characters[item]['name'], 'value': 3})

for key, value in starships.items():
    nodes.append({'id': value['name'], 'class': 'starship', 'group': 3, 'size': 8})

    # films
    for item in value['films']:
        if item in films:
            links.append({'source': value['name'], 'target': films[item]['title'], 'value': 3})

    # characters
    for item in value['pilots']:
        if item in characters:
            links.append({'source': value['name'], 'target': characters[item]['name'], 'value': 3})

for key, value in vehicles.items():
    nodes.append({'id': value['name'], 'class': 'vehicle', 'group': 4, 'size': 8})

    # films
    for item in value['films']:
        if item in films.keys():
            links.append({'source': value['name'], 'target': films[item]['title'], 'value': 3})

    # characters
    for item in value['pilots']:
        if item in characters.keys():
            links.append({'source': value['name'], 'target': characters[item]['name'], 'value': 3})

for key, value in species.items():
    nodes.append({'id': value['name'], 'class': 'species', 'group': 5, 'size': 14})

    # planets
    if value['homeworld'] in planets.keys():
        links.append({'source': value['name'], 'target': planets[value['homeworld']]['name'], 'value': 3})

    # films
    for item in value['films']:
        if item in films.keys():
            links.append({'source': value['name'], 'target': films[item]['title'], 'value': 3})

    # characters
    for item in value['people']:
        if item in characters.keys():
            links.append({'source': value['name'], 'target': characters[item]['name'], 'value': 3})

fw = open('html/sw_data.json', 'w')
fw.write(json.dumps({'nodes': nodes, 'links': links}))
fw.close()
