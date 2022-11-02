import crawl_bangumi
import crawl_reply
import utils
import pandas as pd

if __name__ == '__main__':
    data_md = crawl_bangumi.crawl_bangumi_md("28234419")
    print(data_md)
    data = pd.DataFrame()
    for index, row in data_md.iterrows():
        print("scrapy {}".format(index))
        aid = row['aid']
        bvid = utils.av2bv(aid)
        tmp = crawl_reply.crawl_reply_bv(bvid)
        data = data.append(tmp)
    data.to_csv("./frxiends-1.csv")