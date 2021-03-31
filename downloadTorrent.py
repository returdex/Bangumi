import urllib
import requests
import time
import ssl
import os
from urllib.parse import quote
from urllib import request,error
import  string
import random

'''
防止403
'''
my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]

proxy_list = [
    '175.44.109.221:9999',
    '114.238.9.63:9999',
    '114.99.11.188:1133',
    '115.218.2.254:9000',
    '121.232.199.52:9000',
    '114.239.145.165:9999'
]

timeStr = time.strftime("%Y_%m_%d",time.localtime(time.time())) #新建存放torrent文件夹
folderPath = os.getcwd() + '\\torrent\\' + timeStr
folder = os.path.exists(folderPath)
if not folder:
    os.makedirs(folderPath)

fileTime = time.strftime("%Y_%m_%d",time.localtime(time.time())) #打开并读取文档url
rssLinkFileAddress = "rssLink\\" + fileTime + "rss.txt"
rssFile = open(rssLinkFileAddress, 'r', encoding='utf-8')
urls = rssFile.readlines()
numUrls = len(urls)

for i, url in enumerate(urls):
    header = random.choice(my_headers)
    url = url.replace('\n', '')
    urlStr = url.split('\t')
    fileName = urlStr[0]+'.torrent'
    urlStr[1] = urlStr[1].replace(' ', '%20')
    changeUrl = quote(urlStr[1], safe = string.printable)
    req = urllib.request.Request(changeUrl)
    req.add_header('User-Agent', header)
    try:
        f = urllib.request.urlopen(req)
        data = f.read()
        time.sleep(1)
        with open(folderPath+'\\'+fileName, "wb") as code:
            code.write(data)
        
    except error.HTTPError as e:
        print(e.reason)
        print(e.code)
        print(e.headers)
    except error.URLError as e:
	    print(e.reason)

rssFile.close()