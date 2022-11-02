import json
import time
import requests
from common import REQUEST_INTERVAL

table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
tr = {}
for i in range(58):
    tr[table[i]] = i
s = [11, 10, 3, 8, 4, 6]
xor = 177451812
add = 8728348608


def bv2av(x: str):
    r = 0
    for i in range(6):
        r += tr[x[s[i]]] * 58**i
    return (r-add) ^ xor


def av2bv(x: str):
    x = int(x)
    x = (x ^ xor) + add
    r = list('BV1  4 1 7  ')
    for i in range(6):
        r[s[i]] = table[x//58**i % 58]
    return ''.join(r)


def bv2cid(bv: str) -> [str]:
    """
    利用bv号查询cid号
    :param bv: bv号（以BV开头）
    :return: cid号
    """
    base_url = 'https://api.bilibili.com/x/player/pagelist?bvid={}'
    url = base_url.format(bv)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    time.sleep(REQUEST_INTERVAL)
    response = requests.get(url=url, headers=headers)
    response.encoding = "utf-8"
    if response.status_code == 200:
        data_json = json.loads(response.text)
        if data_json['code'] == 0:
            cid_list = data_json['data']
            cids = [i['cid'] for i in cid_list]
            return cids
        else:
            raise BaseException("No such bv")
    else:
        raise BaseException("Requests Err")


if __name__ == '__main__':
    print(bv2cid("BV1qy4y1q728"))