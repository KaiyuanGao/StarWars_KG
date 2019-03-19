# coding=utf-8
# @author: kaiyuan
# blog: https://blog.csdn.net/Kaiyuan_sjtu

import time
import json


lsts = ['films', 'characters', 'planets', 'starships', 'vehicles', 'species']
data = []
for v in lsts:
    t = []
    with open('data/' + v + '.csv', 'r') as f:
        for line in f:
            tmp = json.loads(line.strip('\n'))
            t.append(tmp)
    data.append(t)
# data= [[films], [c], [p], [st], [v], [sp]

tl = []
for i in range(1, len(lsts)):
    for item in data[i]:
        p = []
        for film in data[0]:
            flag = False
            for f in film[lsts[i]]:
                # 如果角色在电影里出现过
                if item['url'] == f:
                    flag = True
                    break
            if flag:
                p.append(1)
            else:
                p.append(0)
        tl.append({'name': item['name'], 'type': data[i], 'group': i-1, 'vector': p})


films = [[data[0][x]['title'], data[0][x]['release_date']] for x in range(0, len(data[0]))]
result = {'films': films, 'data': tl}

fw = open('html/timeline.json', 'w')
fw.write(json.dumps(result))
fw.close()
