# coding=utf-8
# @author: kaiyuan
# blog: https://blog.csdn.net/Kaiyuan_sjtu
"""
爬取星战系列电影的五大类实体
保存data文件夹下
"""

from urllib import request
import json

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

with open('data/films.csv', 'r') as f:
    films = []
    for line in f:
        line = json.loads(line.strip('\n'))
        films.append(line)

# 获取实体信息：characts，planets，starships，vehicles，species
targets = ['characters', 'planets', 'starships', 'vehicles', 'species']
for target in targets:
    f = open('data/' + target + '.csv', 'w')
    data = []
    for item in films:
        tmp = item[target]
        for t in tmp:
            if t in data:
                continue
            else:
                data.append(t)

            while 1:
                print(t)
                try:
                    req = request.Request(url=t, headers=headers)
                    response = request.urlopen(req, timeout=20)
                    result = response.read()
                except Exception:
                    continue
                else:
                    f.write(result.decode() + '\n')
                    break
                finally:
                    pass

    print(str(len(data)) + ' ' + target)
    f.close()

