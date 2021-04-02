import feedparser
import time
import xlwt
import os

path = os.path.abspath(os.path.dirname(__file__))
path = path + '\\rssLink'
folder = os.path.exists(path)
if not folder:
    os.makedirs(path)

fileTime = time.strftime("%Y_%m_%d",time.localtime(time.time()))
fileAddress = 'rssLink\\' + fileTime + "rss.txt"
rssFile = open(fileAddress, 'w', encoding='utf-8')

rssSubscribe = feedparser.parse('https://bangumi.moe/rss/latest')

for entry in rssSubscribe['entries']:
    title = entry.title.replace('/', '_')
    rssFile.write(title)
    rssFile.write('\t')
    rssFile.write(entry.enclosures[0].href)
    rssFile.write('\n')

rssFile.close()