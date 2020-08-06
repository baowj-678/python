import requests
import re
def get_one_page(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            response.encoding=response.apparent_encoding
            return response.text
        return None
    except:
        return None
def parse_one_page(html):
    pattern=re.compile('<dd>.*?board-index-(.*?)">.*?<p class="name"><a.*?title="(.*?)" data.*?star">\s*(.*?)\s*</p>.*?time">(.*?)</p>',re.S)
    item=re.findall(pattern,html)
    print(item)
    print('\n')

def main(offset):
    url='http://movie.douban.com/top250'
    html=get_one_page(url)
    print(html)

'''for i in range(10):
    main(i*10)'''
main(25)