# coding=utf-8
# @author: kaiyuan
# blog: https://blog.csdn.net/Kaiyuan_sjtu
"""
可视化数据
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fr = open('data/films.csv', 'r')
fw = open('data/war_basic.csv', 'w')
fw.write('title,key,value\n')
for line in fr:
    line = json.loads(line.strip('\n'))
    fw.write(line['title'] + ',' + 'characters,' + str(len(line['characters'])) + '\n')
    fw.write(line['title'] + ',' + 'planets,' + str(len(line['planets']))+ '\n')
    fw.write(line['title'] + ',' + 'starships,' + str(len(line['starships']))+ '\n')
    fw.write(line['title'] + ',' + 'vehicles,' + str(len(line['vehicles']))+ '\n')
    fw.write(line['title'] + ',' + 'species,' + str(len(line['species']))+ '\n')
fr.close()
fw.close()

war_data = pd.read_csv('data/war_basic.csv')

fig, ax = plt.subplots(1,1)

sns.set_style("whitegrid")

sns.palplot(sns.color_palette('hls',8))

sns_plot = sns.barplot(x="key", y="value", hue="title", data=war_data, ax=ax,
            palette=sns.color_palette("hls", 8))
fig = sns_plot.get_figure()
ax.set_title('Star Wars Entity Statistics')

fig.savefig('data/Star Wars Entity Statistics.png')

plt.show()
