import requests
import re
import sys
import json
import codecs
reload(sys)
#sys.setdefaultencoding("utf-8")

class Spider(object):
    def __init__(self):
        print("Scarpy is starting")
    def getSource(self, url):
        html = requests.get(url)
        return html.text
    def parse(self, html):
        info = []
        a = re.search('>(.*?)</a></h3>', html,re.S).group(1)
        #a = a.decode('utf-8')
        print(a)
        info.append(a + '\n')
        return a
if __name__ == '__main__':
    info = []
    HTML2 = []
    spider = Spider()
    #url = "http://litaotao.github.io/python-materials?s=byr"
    url = "https://www.engineeringvillage.com/search/results/quick.url?CID=quickSearchCitationFormat&database=1&SEARCHID=64b35224Mb3d9M40b7Mad1aM5b87dfa49df3&intialSearch=true"
    html = spider.getSource(url)
    #print(html)
    #HTML2 = re.findall('<h2 id=".*">.*</h2>', html)
    HTML2 = re.findall('<h3 class="resulttitle">.*</h3>', html)
    print(HTML2)
    for each in HTML2:
        a = spider.parse(each)
        print(a)
        info.append(a)
    print info
f = codecs.open('F:\Python\Scrapy\Title.txt', 'a', 'utf-8')
f.writelines(info)



