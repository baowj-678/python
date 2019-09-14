import requests
from bs4 import BeautifulSoup
import re
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return None

def getmInfo(url):
    for i in range(10):
        num=str(10*i)
        URL=url+'?offset='+num
        html=getHTMLText(URL)
        name=re.findall('board-index-(.*?)">[\s\S]*?<p class="name"><a href=".*?tle="(.*?)" da[\s\S]*?主演：(.*?)\n[\s\S]*?"releasetime">(.*?)</p> ',html)
        for j in name:
            print(j)



def main():
    url='https://maoyan.com/board/4'
    getmInfo(url)

main()
