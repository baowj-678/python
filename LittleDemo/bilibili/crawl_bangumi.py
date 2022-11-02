# coding=utf-8
import json
import time
import pandas as pd
import requests


def crawl_bangumi_ep(ep: str) -> pd.DataFrame:
    """
    使用ep号爬取番剧所有aid和其他信息
    :param ep: 番剧的ep号
    :return: pandas.DataFrame
    """
    pass


def crawl_bangumi_md(md: str) -> pd.DataFrame:
    """
    使用ep号爬取番剧所有aid和其他信息
    :param md: 番剧的md号（只包含数字）
    :return: pandas.DataFrame
    """
    base_url = "https://api.bilibili.com/pgc/review/user?media_id={}"
    url = base_url.format(md)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    response = requests.get(url=url, headers=headers)
    response.encoding = "utf-8"
    if response.status_code == 200:
        data_json = json.loads(response.text)
        print(response.text)
        if data_json['code'] == 0:
            ssid = data_json['result']['media']['season_id']
            time.sleep(0.5)
            return crawl_bangumi_ssid(ssid)
        else:
            raise BaseException("No such md")
    else:
        raise BaseException("Requests Err")


def crawl_bangumi_ssid(ssid: str) -> pd.DataFrame:
    base_url = "https://api.bilibili.com/pgc/web/season/section?season_id={}"
    url = base_url.format(ssid)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    response = requests.get(url=url, headers=headers)
    response.encoding = "utf-8"
    if response.status_code == 200:
        data_json = json.loads(response.text)
        if data_json['code'] == 0:
            data_list = data_json['result']['main_section']['episodes']
            data_pd = pd.DataFrame(data_list)
            return data_pd
        else:
            return None
    else:
        return None


if __name__ == '__main__':
    for i in range(100):
        print("\r进度{}".format(i), end='')
        time.sleep(0.3)
