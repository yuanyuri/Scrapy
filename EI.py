#coding utf-8
import re
import requests



class Spider(object):
    def __init__(self):
        print("scrapy is starting:")

    def get_HTML(self, url):
        source = requests.get(url)
        return source.text

    def parse(self, html):
        #print(html)
        title = re.search('href=.*>(.*?)</a></h3>', html).group(1)
        #print(title)
        return title

    def extract(self, html):
        info = []
        #section = re.findall('<div class="resultcontent">.*</div>', html, re.S)
        #print(section)
        section = re.findall('<h3 class="resulttitle">.*</h3>', html)
        for each in section:
            a = self.parse(each)
            info.append(a)
        return info

if __name__ == "__main__":
    spider = Spider()
    url = "https://www.engineeringvillage.com/search/results/quick.url?CID=quickSearchCitationFormat&database=1&SEARCHID=aeb7acaaM5e74M41c6Ma735M58d4d036876a&intialSearch=true"
    html = spider.get_HTML(url)
    #print (html)
    paper = spider.extract(html)
    print(paper)
    filename = './paper.txt'
    f = open(filename, 'w')
    for each in paper:
        f.write(each + "\n")
    f.close()
