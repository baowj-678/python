import requests
from lxml import etree


url = 'https://comment.bilibili.com/183909438.xml'
response = requests.get(url).content
html = etree.HTML(response)
content = html.xpath('//d//text()')

print(content)
