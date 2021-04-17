import feedparser
import time
import os
import analysis
import json

path = os.path.abspath(os.path.dirname(__file__))
path = path + '\\rssLink'
folder = os.path.exists(path)
if not folder:
    os.makedirs(path)

fileTime = time.strftime("%Y_%m_%d",time.localtime(time.time()))
fileAddress = 'rssLink\\' + fileTime + "rss.json"
rssFile = open(fileAddress, 'w', encoding='utf-8')

rssSubscribe = feedparser.parse('https://bangumi.moe/rss/latest')
rssFile.write('[' + '\n')

i=1
for entry in rssSubscribe['entries']:
    value = analysis.rss(entry)
    valueJson = value.saveToJson()
    #print(json.dumps(valueJson, ensure_ascii=False))
    #print(valueJson)
    #print('\n')
    if i>1:
        rssFile.write(',')

    rssFile.write(valueJson)
    rssFile.write('\n')
    i += 1

rssFile.write(']')
rssFile.close()