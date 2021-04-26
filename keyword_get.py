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
        threads.append(threading.Thread(target=download_json_image, args=(i, path)))
    for i in threads:
        i.start()
    for i in threads:
        i.join()


def ask_url(url, path, number=10):
    i = 0
    post_ids = []
    js = get_json(url.format(i))
    while True:
        # posts 没有内容时，退出
        if not js['posts']:
            break
        for post_id_i in js['posts']:
            post_ids.append(post_id_i['postID'])
            i += 1
        # 指定爬取页数
        # print(post_ids)
        number -= 1
        if number % 10 == 0:
            multi_thread(idlist=post_ids, path=path)
            if number == 0:
                break
            post_ids = []
        js = get_json(url.format(js['start']))
    print("爬取完成, 共{} 个帖子".format(i))


def search_key(keyword):
    # 提供一组 _key: 074A517999865CB0A3DC24034F244DEB1E23E1512BA28A8D07315737041A1E393A13114A41B9FCE24CBD95E0AF7E0C72DC99A8E24218CC70
    # _key = input("请输入 _key: ")
    _key = "074A517999865CB0A3DC24034F244DEB1E23E1512BA28A8D07315737041A1E393A13114A41B9FCE24CBD95E0AF7E0C72DC99A8E24218CC70"
    url = "http://floor.huluxia.com/post/search/ANDROID/2.1?platform=2&market_id=tool_baidu&_key" \
          "=%s&start=1&count=20&cat_id=56&keyword=%s&flag=0" % (_key, parse.quote(keyword))
    # print(url)
    ask_url(url, 'search_result/')


if __name__ == '__main__':
    pass