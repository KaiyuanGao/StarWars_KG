# coding=utf-8
# @author: kaiyuan
# blog: https://blog.csdn.net/Kaiyuan_sjtu
"""
获取七部电影的所有信息，以字典形式保存
对应的数据存储在html/all_data.json中
"""
import json
data = {}
lsts = ['films', 'characters', 'planets', 'starships', 'vehicles', 'species']
for v in lsts:
    with open('data/' + v + '.csv', 'r') as f:
        for line in f:
            tmp = json.loads(line.strip('\n'))
            if v == 'films':
                data[tmp['title']] = tmp
                print(tmp['title'], tmp)
            else:
                data[tmp['name']] = tmp

fw = open("html/all_data.json", "w")
fw.write(json.dumps(data))
fw.close()