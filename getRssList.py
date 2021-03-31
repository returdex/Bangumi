import feedparser
import time
import xlwt

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