# coding=utf-8
import requests
from lxml import etree
import pandas as pd


def crawl_comment(cid: str) -> pd.DataFrame:
    """ 获取弹幕内容
    :param cid: 弹幕池的cid号
    :return: pandas['comment', 'show-time', 'mode', 'font-size', 'font-color',
                   'publish-time', 'pool', 'uid', 'row-id', 'none']
    """
    url = 'http://comment.bilibili.com/{}.xml'.format(cid)
    columns = ['comment', 'show-time', 'mode', 'font-size', 'font-color', 'publish-time', 'pool', 'uid', 'row-id',
               'none']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    response = requests.get(url=url, headers=headers)
    tree = etree.HTML(response.content)
    message = tree.xpath('//d/text()')
    infos = tree.xpath('//d/@p')
    comment = [info.split(',') for info in infos]
    data = [[i[0], *i[1]] for i in zip(message, comment)]
    data = pd.DataFrame(data=data, columns=columns)
    return data


if __name__ == "__main__":
    pass
