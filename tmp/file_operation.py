#!/usr/bin/python3
# coding = utf-8
"""
@author:m1n9yu3
@file:file_operation.py
@time:2021/01/13
"""

import os


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



if __name__ == '__main__':
    pass
