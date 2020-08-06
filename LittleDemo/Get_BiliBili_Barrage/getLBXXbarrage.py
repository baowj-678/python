import requests
from lxml import etree


def getContent(cid: str):
    url = 'https://comment.bilibili.com/' + cid + '.xml'
    print(url)
    response = requests.get(url).content
    html = etree.HTML(response)
    content = html.xpath('//d//text()')
    return content


if __name__ == '__main__':
    cids = None
    barrages = []
    with open('LittleDemo/GetBiliBiliBarrage/lbxx-cid.txt',
              mode='r',
              encoding='utf-8') as file:
        cids = file.readlines()
        cids = [cid.strip() for cid in cids]
        # print(cids)
    for cid in cids:
        barrages = barrages + getContent(cid)
    with open('LittleDemo/GetBiliBiliBarrage/lbxx-barrage.txt',
              mode='w+',
              encoding='utf-8') as file:
        file.write('\n'.join(barrages))
