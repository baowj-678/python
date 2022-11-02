import pandas as pd
import requests
import os
import time
import json

# cookie
cookie = ""
# save path
file_dir = "./"
# columns
columns = ["time", "like", "uid", "uname", "sex", "message"]


# 1:评论(楼层);
# 2:最新评论(时间);
# 3:热门评论(热度)
reply_mode = 3


def visit_bv(bv):
    """ 访问BV对应的网页,查看是否存在 """
    url = 'https://www.bilibili.com/video/' + bv
    headers = {
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9',
        'referer': 'https://www.bilibili.com/',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 404 or """<div class="error-text">啊叻？视频不见了？</div>""" in response.text:
        print('视频不存在!')
        return False
    else:
        return True


def b2a(bv):
    """ BV -> av """
    if bv[:2] == 'av':
        return bv[2:]
    bv = list(bv[2:])
    keys = {'1': 13, '2': 12, '3': 46, '4': 31, '5': 43, '6': 18, '7': 40, '8': 28, '9': 5,
            'A': 54, 'B': 20, 'C': 15, 'D': 8, 'E': 39, 'F': 57, 'G': 45, 'H': 36, 'J': 38, 'K': 51, 'L': 42, 'M': 49,
            'N': 52, 'P': 53, 'Q': 7, 'R': 4, 'S': 9, 'T': 50, 'U': 10, 'V': 44, 'W': 34, 'X': 6, 'Y': 25, 'Z': 1,
            'a': 26, 'b': 29, 'c': 56, 'd': 3, 'e': 24, 'f': 0, 'g': 47, 'h': 27, 'i': 22, 'j': 41, 'k': 16, 'm': 11,
            'n': 37, 'o': 2, 'p': 35, 'q': 21, 'r': 17, 's': 33, 't': 30, 'u': 48, 'v': 23, 'w': 55, 'x': 32, 'y': 14,
            'z': 19}
    for i in range(len(bv)):
        bv[i] = keys[bv[i]]
    bv[0] *= (58 ** 6)
    bv[1] *= (58 ** 2)
    bv[2] *= (58 ** 4)
    bv[3] *= (58 ** 8)
    bv[4] *= (58 ** 5)
    bv[5] *= (58 ** 9)
    bv[6] *= (58 ** 3)
    bv[7] *= (58 ** 7)
    bv[8] *= 58
    return str((sum(bv) - 100618342136696320) ^ 177451812)


def get_reply_json(bv, nexts=0, mode=3):
    """ 获取评论json
        bv: bv号
        nests: json页码
        mode: 1楼层,2时间,3热门
    """
    r_url = 'https://api.bilibili.com/x/v2/reply/main'
    url = 'https://www.bilibili.com/video/{}'.format(bv)
    av = b2a(bv)
    param = {
        'jsonp': 'jsonp',
        'next': nexts,  # 页码
        'type': '1',
        'oid': av,  # av号
        'mode': mode,  # 1:楼层大前小后, 2:时间晚前早后, 3:热门评论
        'plat': '1',
        '_': str(time.time() * 1000)[:13],  # 时间戳
    }
    return send_request(url, r_url, param)


def get_sub_reply_json(bv, rpid, pn=1):
    """ 返回子评论json
        bv: bv号
        rpid: 父评论的id
        pn: 子评论的页码
    """

    r_url = 'https://api.bilibili.com/x/v2/reply/reply'
    url = 'https://www.bilibili.com/video/' + bv
    av = b2a(bv)
    param = {
        # 'callback': 'jQuery172040348849791483166_' + str(time.time()*1000)[:13],
        'jsonp': 'jsonp',
        'pn': pn,  # pagenumber
        'type': '1',
        'oid': av,
        'ps': '10',
        'root': rpid,  # 父评论的rpid
        '_': str(time.time() * 1000)[:13],  # 时间戳
    }
    return send_request(url, r_url, param)


def send_request(ref_url, reply_url, param):
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': cookie,
        'pragma': 'no-cache',
        'referer': ref_url,
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    }
    response = requests.get(reply_url, headers=headers, params=param)
    response.encoding = 'utf-8'

    # 将得到的json文本转化为可读json
    if 'code' in response.text:
        c_json = json.loads(response.text)
    else:
        c_json = {'code': -1}
    if c_json['code'] != 0:
        print('error! status_code:{}, text:{}'.format(response.status_code, response.text))
        return None
    return c_json


def get_piece_reply(item):
    ret = [
        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item['ctime'])),  # 时间
        item['like'],  # 赞数
        item['member']['mid'],  # uid
        item['member']['uname'],  # 用户名
        item['member']['sex'],  # 性别
        item['content']['message']  # 评论
    ]
    return ret


def parse_sub_reply(bv, rpid):
    """ 解析子评论json
        bv: bv号
        rpid: reply_id
    """
    time.sleep(0.5)
    cr_json = get_sub_reply_json(bv, rpid)['data']
    count = cr_json['page']['count']
    sub_data = []
    for pn in range(1, (count + 9) // 10 + 1):
        print('sub page:%d / total pieces %d' % (pn, count))
        cr_json = get_sub_reply_json(bv, rpid, pn=pn)['data']
        cr_list = cr_json['replies']
        if cr_list:  # 有时'replies'为'None'
            for item in cr_list:
                sub_data.append(get_piece_reply(item))
        time.sleep(0.5)
    return sub_data


def parse_reply(bv: str) -> []:
    """ 解析评论json """
    c_json = get_reply_json(bv, mode=reply_mode)
    if c_json:
        # 总评论数
        try:
            count_all = c_json['data']['cursor']['all_count']
            print('回复数总计：%d' % count_all)
        except KeyError:
            print('该视频可能没有评论!')
            return []
    else:
        print('json错误')
        return []

    # 置顶评论
    if c_json['data']['top']['upper']:
        reply_top = c_json['data']['top']['upper']
        data = [get_piece_reply(reply_top)]
        if reply_top['rcount'] or ('replies' in reply_top and reply_top['replies']):
            rpid = reply_top['rpid']  # 父评论的rpid
            data += parse_sub_reply(bv, rpid)
    else:
        data = []
    # 开始序号
    count_next = 0

    for page in range((count_all + 19) // 20):
        print('page: %d' % (page + 1))
        c_json = get_reply_json(bv, count_next, mode=reply_mode)
        if not c_json:
            raise "get_reply_json None"
        # 评论列表
        c_list = c_json['data']['replies']
        # 有评论,就进入下面的循环保存
        if c_list:
            for item in c_list:
                print("reply count:%d" % len(data))
                reply_temp = get_piece_reply(item)
                # 获取子评论
                has_sub_replies = False
                if item['rcount'] or ('replies' in item and item['replies']):
                    has_sub_replies = True
                    rpid = item['rpid']
                data.append(reply_temp)
                # 如果有回复评论,爬取子评论
                if has_sub_replies:
                    data += parse_sub_reply(bv, rpid)
            if c_json['data']['cursor']['is_end']:
                print('读取完毕,结束')
                break
            if c_json['data']['cursor']['next'] != count_next:
                count_next = c_json['data']['cursor']['next']
        else:
            print('评论为空,结束!')
            break
        time.sleep(0.5)
    return data


def crawl_reply_bv(bv: str) -> pd.DataFrame:
    """
    通过bv号爬取该视频所有评论
    :param bv:
    :return: pandas.DataFrame
    """
    if not visit_bv(bv):
        raise "视频不存在"
    data_list = parse_reply(bv)
    data_pd = pd.DataFrame(data=data_list, columns=columns)
    print("爬取 {} 评论成功!".format(bv))
    return data_pd


def main():
    global file_dir

    bv = "BV1W14y1b7Mq"
    if not visit_bv(bv):
        print("视频不存在")
        return

    data = parse_reply(bv)
    pd_data = pd.DataFrame(data=data, columns=columns)
    pd_data.to_csv(file_dir + "BV1W14y1b7Mq_reply.csv")


if __name__ == "__main__":
    main()
    # print(parse_sub_reply("BV1Fa411S7pR", "122999842288"))


