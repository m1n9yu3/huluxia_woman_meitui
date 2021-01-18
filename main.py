#!/usr/bin/python3
# coding = utf-8
"""
@author:m1n9yu3
@file:main.py
@time:2021/01/12
"""

import threading
from get_data import *
from keyword_get import ask_url, search_key

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
        threads.append(threading.Thread(target=parse_json, args=(start_id + i,)))
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
        parse_json(post_id, './img/')
    else:
        parse_json(post_id, './{}/'.format(path))


def main():
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
    main()
