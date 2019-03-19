# coding=utf-8
# @author: kaiyuan
# blog: https://blog.csdn.net/Kaiyuan_sjtu
"""
获取星战电影七部的所有信息
一行存储一步电影信息
"""

from urllib import request

films = []
for x in range(1, 8):
    films.append('http://swapi.co/api/films/' + str(x) + '/')

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

f = open('data/films.csv', 'w', encoding='utf-8')
for item in films:
    req = request.Request(url=item, headers=headers)
    response = request.urlopen(req, timeout=20)
    result = response.read()
    print(result)
    f.write(result.decode() + '\n')
f.close()


