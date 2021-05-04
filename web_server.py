#!/usr/bin/python3
# encoding: utf-8
"""
@author: m1n9yu3
@license: (C) Copyright 2021-2023, Node Supply Chain Manager Corporation Limited.
@file: web_server.py
@time: 2021/4/27 13:41
@desc:
"""


from flask import *
from huluxiaThirdflood_api import get_random_imageurl

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/image/<num>')
def displayImage(num):
    # print(num)
    imageurllist = get_random_imageurl(int(num))
    return  render_template('images.html', imagelist=imageurllist)

if __name__ == '__main__':
    app.run(debug=True)
