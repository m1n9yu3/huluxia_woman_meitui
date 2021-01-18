#!/usr/bin/python3
# coding = utf-8
"""
@author:m1n9yu3
@file:keyword_get.py
@time:2021/01/13
"""

from get_data import *
import threading
from urllib import parse


def multi_thread(idlist, path):
    """线程控制 ， 一次跑 1000 个线程"""
    # for i in range(start_id, step+start_id):
    #     parse_json(url, start_id+i)
    threads = []
    for i in idlist:
        threads.append(threading.Thread(target=parse_json, args=(i,path)))
    for i in threads:
        i.start()
    for i in threads:
        i.join()


def ask_url(url, path):
    count = 0
    i = 1
    while True:
        js = get_json(url.format(i))
        post_ids = []
        if not js['posts']:
            print("爬取完成, 共{} 个帖子".format(i))
            return
        for post_id_i in js['posts']:
            post_ids.append(post_id_i['postID'])
        # print(post_ids)

        count += 1
        i += 20
        if count == 50:
            count = 0
            multi_thread(idlist=post_ids, path=path)


def search_key(keyword):
    # 提供一组 _key: 074A517999865CB0A3DC24034F244DEB1E23E1512BA28A8D07315737041A1E393A13114A41B9FCE24CBD95E0AF7E0C72DC99A8E24218CC70
    _key = input("请输入 _key: ")
    url = "http://floor.huluxia.com/post/search/ANDROID/2.1?platform=2&market_id=tool_baidu&_key" \
          "=%s&start=1&count=20&cat_id=56&keyword=%s&flag=0" % (_key, parse.quote(keyword))
    # print(url)
    ask_url(url)
