#!/usr/bin/python3
# coding = utf-8
"""
@author:m1n9yu3
@file:get_data.py
@time:2021/01/13
"""

import requests
from file_operation import *
import time
import json

# 代理 ip 爬取
proxies = {"http": "127.0.0.1:8889"}


def get_json(url):
    return requests.get(url, proxies=proxies).json()


def download_img(path, data):
    """图片下载 评论中图片和主图图片"""

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

    for i in data:
        download_signed_img(i)


def download_video(path, url):
    """视频下载"""
    response = requests.get(url)
    with open(path, "wb") as f:
        f.write(response.content)


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
                download_img(js_dir, js['post']['images'])
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
                download_img(js_dir, i['images'])
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


if __name__ == '__main__':
    pass
