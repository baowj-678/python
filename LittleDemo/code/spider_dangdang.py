from selenium import webdriver
import re
browser=webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

def getpage(url):
    browser.get(url)
    html=browser.page_source
    
    print(len(html))
    return html

def getinfo(html):
    try:
        result=re.findall('<a title="(.*?)".*?<span class="preis">(.*?)</span>.*?authorname">(.*?)</p>',html,re.S) 
        for i in range(25):
            print(result[i])
    except:
        pass

    
def main():
    for i in range(36):
        url = "http://store.dangdang.com/255/list.html?sort_type=sort_xsellcount_desc&inner_cat=10000002550120003&page_index="
        url0 = "#pos"
        html=getpage(url + str(i+1) + url0)
        getinfo(html)
    
main()
browser.close()
