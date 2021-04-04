import re
import os

class rss:
    name = '' #番名
    link = '' #链接
    group = '' #字幕组
    __linkType = '' #磁链 或者bittorrent下载链接
    def __init__(self, entry):
        
        if entry.title[0] == "[":
            temp = re.findall(r'[[](.*?)[]]', entry.title)
        else:
            temp = re.findall(r'[【](.*?)[】]', entry.title)
        
        try:
            self.group = "".join(temp[0])
        except IndexError:
            self.group = "".join(temp)
        
        temp1 = '[' + self.group + ']'
        self.name = entry.title.lstrip(temp1)
        self.link = entry.enclosures[0].href
        strIndex = self.link.find('magnet')
        if strIndex >= 0:
            __linkType = 'magnet'
        else:
            __linkType = 'torrent'
    
    def print(self):
        print(self.group)
        print(self.name)
        print(self.link)
        print(self.__linkType)
