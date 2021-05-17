#!/usr/bin/python3
# encoding: utf-8
"""
@author: m1n9yu3
@license: (C) Copyright 2021-2023, Node Supply Chain Manager Corporation Limited.
@file: huluxiaThirdflood_api.py
@time: 2021/4/26 19:03
@desc:
"""

import os
import requests
import time
import json
import threading
from urllib import parse


# 操作文件 api
def mkdir_(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def remove_(path):
    if os.path.isfile(path):
        os.remove(path)


def save_text(path, context):
    """保存 txt 文档"""
    with open(path, "a") as f:
        f.write(str(context))


#  获取数据操作

# 代理 ip 爬取
# proxies = {"http": "127.0.0.1:8889"}
proxies = {}


def get_json(url):
    return requests.get(url, proxies=proxies).json()


def download_img(path, data, flag):
    """图片下载 评论中图片和主图图片
    :param flag:
    """

    def download_signed_img(url):
        """ 单个图片下载"""
        # print(urls)
        url = url.replace(" ", "")  # 替换空格
        img_name = path + url.split("/")[-1]
        if img_name.split('.')[-1] == 'ht':
            img_name += '.png'
        with open(img_name, 'wb') as f:
            f.write(requests.get(url, proxies=proxies).content)
            # print("爬取完成:", url)

    if flag != 0:
        return data
    for i in data:
        download_signed_img(i)


def download_video(path, url):
    """视频下载"""
    return
    response = requests.get(url)
    with open(path, "wb") as f:
        f.write(response.content)


def download_json_image(post_id, flag=''):
    """数据解析，并下载图片."""
    # 帖子详细信息链接
    url = "http://floor.huluxia.com/post/detail/ANDROID/2.3?platform=2&market_id=tool_baidu&post_id={}&page_no={}"
    try:
        print(post_id, "开始爬取")
        page_num = 1
        js_dir = ''
        while page_num <= 50:
            js = get_json(url.format(post_id, page_num))
            # 打印测试数据
            # print(url.format(post_id, page_num))
            # print(js)

            if js['msg'] == '话题不存在' or js['msg'] == '话题所属分类不存在':
                return
            # 判断页 是否结束
            if page_num > 1:
                if not js['comments']:
                    break
            # 开始保存图片数据
            if page_num == 1:
                # 创建目录
                if flag != '':
                    js_dir = flag
                    mkdir_(js_dir)
                else:
                    js_dir = './{}/'.format(js['post']['category']['title'])
                    mkdir_(js_dir)  # 版块目录
                    js_dir += '{}/'.format(post_id)
                    mkdir_(js_dir)  # post_id 目录，二级目录
                # 采集首页图片
                download_img(js_dir, js['post']['images'], 0)
                txt_name = js_dir + "说明.txt"
                # 并将 数据进行采集
                save_text(txt_name, js['post']['title'] + '\n' + js['post']['detail'])

                # 判断是否有视频 ，有视频下载视频
                if js['post']['voice'] != "":
                    d = json.loads(js['post']['voice'])
                    download_video(js_dir + d['videofid'].split('/')[-1] + '.mp4', d['videohost'] + d['videofid'])

            # 保存每一个帖子的 json 数据
            save_text(js_dir + "js.txt", js)
            # 采集 评论图片
            for i in js['comments']:
                download_img(js_dir, i['images'], 0)
            # 采集评论 文字

            page_num += 1
        print(post_id, "爬取结束")
        return
    except Exception as e:
        with open("log.txt", mode="a") as f:
            content = "current:{} \npost_id: {}\n error_content:{} \n\n".format(
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), post_id, e)
            f.write(content)
        return

def parse_json(post_id, flag=''):
    """数据解析，并下载图片."""
    # 帖子详细信息链接
    url = "http://floor.huluxia.com/post/detail/ANDROID/2.3?platform=2&market_id=tool_baidu&post_id={}&page_no={}"
    try:
        print(post_id, "开始爬取")
        page_num = 1
        js_dir = ''
        while page_num <= 50:
            js = get_json(url.format(post_id, page_num))
            # 打印测试数据
            # print(url.format(post_id, page_num))
            # print(js)

            if js['msg'] == '话题不存在' or js['msg'] == '话题所属分类不存在':
                return
            # 判断页 是否结束
            if page_num > 1:
                if not js['comments']:
                    break
            # 开始保存图片数据
            if page_num == 1:
                # 采集首页图片
                download_img(js_dir, js['post']['images'], 0)
                # 并将 数据进行采集

                # 判断是否有视频 ，有视频下载视频
                if js['post']['voice'] != "":
                    d = json.loads(js['post']['voice'])
                    download_video(js_dir + d['videofid'].split('/')[-1] + '.mp4', d['videohost'] + d['videofid'])

            # 采集 评论图片
            for i in js['comments']:
                download_img(js_dir, i['images'], 0)

            page_num += 1
        print(post_id, "爬取结束")
        return
    except Exception as e:
        with open("log.txt", mode="a") as f:
            content = "current:{} \npost_id: {}\n error_content:{} \n\n".format(
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), post_id, e)
            f.write(content)
        return



def get_images_url(post_id, flag=''):
    """数据解析，并下载图片."""
    # 帖子详细信息链接
    url = "http://floor.huluxia.com/post/detail/ANDROID/2.3?platform=2&market_id=tool_baidu&post_id={}&page_no={}"
    try:
        page_num = 1
        js_dir = ''
        image_url_list = []
        while page_num <= 50:
            js = get_json(url.format(post_id, page_num))


            if js['msg'] == '话题不存在' or js['msg'] == '话题所属分类不存在':
                return
            # 判断页 是否结束
            if page_num > 1:
                if not js['comments']:
                    break
            # 开始保存图片数据
            if page_num == 1:
                # 采集首页图片
                image_url_list += download_img(js_dir, js['post']['images'], 1)

            # 采集 评论图片
            for i in js['comments']:
                image_url_list += download_img(js_dir, i['images'], 1)
            # 采集评论 文字

            page_num += 1
        return image_url_list
    except Exception as e:
        with open("log.txt", mode="a") as f:
            content = "current:{} \npost_id: {}\n error_content:{} \n\n".format(
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), post_id, e)
            f.write(content)
        return []

def set_proxy(proxy: dict):
    """用于设置代理"""
    global proxies
    proxies = proxy


def multi_thread(idlist, path):
    """线程控制 ， 一次跑 1000 个线程"""
    # for i in range(start_id, step+start_id):
    #     parse_json(url, start_id+i)
    threads = []
    for i in idlist:
        threads.append(threading.Thread(target=get_images_url, args=(i, path)))
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






def get_random_imageurl(num:int) -> list:
    url = "http://floor.huluxia.com/post/list/ANDROID/2.1?platform=2&market_id=tool_baidu&start={}&count=20&cat_id=56&tag_id=0&sort_by=0"
    i = 0
    number = num
    image_url_list = []
    js = get_json(url.format(i))
    if not js['posts']:
        return []
    post_list = js['posts']
    while True:
        # 判断是否使用完毕
        if len(post_list) == 0:
            js = get_json(url.format(js['start']))
            if not js['posts']:
                break
            post_list = js['posts']
            i = 0

        image_url_list += get_images_url(post_list[i]['postID'])
        i += 1
        # 指定爬取页数
        number -= 1
        if len(image_url_list) >= num:
            break

        print(image_url_list)
    # print("爬取完成, 共{} 个帖子".format(i))
    return image_url_list





'''
target : 目标
http://floor.huluxia.com/post/detail/ANDROID/2.3?platform=2&market_id=tool_baidu&post_id={帖子id}&page_no={页数}

帖子id 依次递增

'''


def section_multi_thread(start_id, step):
    """线程控制 ， 一次跑 1000 个线程"""
    # for i in range(start_id, step+start_id):
    #     parse_json(url, start_id+i)
    threads = []
    for i in range(step):
        threads.append(threading.Thread(target=download_json_image, args=(start_id + i,)))
    for i in threads:
        i.start()
    for i in threads:
        i.join()


def section_get():
    url = "http://floor.huluxia.com/post/detail/ANDROID/2.3?platform=2&market_id=tool_baidu&post_id={}&page_no={}"

    # 收集初始化数据
    section = input("请输入区间: start-end (start >= 1, end > start)")
    start = int(section.split('-')[0])
    end = int(section.split('-')[1])
    thread_num = int(input("请输入线程数量:"))

    # 开始爬取
    step = 1000  # 设置线程数量
    for i in range(start, end, thread_num):
        # parse_json(url, i)
        # 下一个目标，尝试多线程优化
        section_multi_thread(url, i, thread_num)
    # 爬取记录 ：  2021.1.13, 8:00  爬取到 24000 post_id


def get_leg():
    """获取美腿图片"""
    path = input("请输入爬取路径，仅支持已存在的目录，或者单级目录:")
    try:
        page_num = int(input("请输入页数,页数越大，爬的越慢:"))
    except ValueError:
        page_num = 5
    url = "http://floor.huluxia.com/post/list/ANDROID/2.1?platform=2&market_id=tool_baidu&start={}&count=20&cat_id=56&tag_id=0&sort_by=0"
    if path[-1] != '/':
        path += '/'
    ask_url(url, path, page_num)


def get_post_id():
    post_id = int(input("请输入 post id："))
    path = input("请输入目录,输入q ,则保存到默认目录：")
    if path == 'q':
        download_json_image(post_id, './img/')
    else:
        download_json_image(post_id, './{}/'.format(path))


def menu():
    # 清除日志  爬取过程中出现的错误
    remove_("log.txt")
    """主模块菜单，将所有功能集合成一个菜单"""
    while True:
        print("------菜单-------")
        print("1. 区间爬取")
        print("2. 爬取美腿图片")
        print("3. 关键字爬取")
        print("4. 爬取 post_id 对应的帖子")
        print("5. 设置代理")
        print("q. 退出菜单")
        set_proxy(None)
        flag = input("请输入你的选项:")
        if flag == '1':
            section_get()
        elif flag == '2':
            get_leg()
        elif flag == '3':
            keyword = input("请输入关键字:")
            search_key(keyword)
        elif flag == '4':
            get_post_id()
        elif flag == '5':
            http_ip = input("请输入: 代理ip地址:端口 ")
            set_proxy({"http": http_ip})
        elif flag == 'q':
            break



if __name__ == '__main__':
    pass