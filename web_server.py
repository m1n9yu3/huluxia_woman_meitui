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
import conf

app = Flask(__name__)


@app.route('/')
def hello_world():
    # 爬取 12 个帖子
    image_list = get_random_imageurl(conf.display_num)
    # print(image_list)
    display_image = []
    for i in range(0, len(image_list), 3):
        try:
            display_image.append([["#imageModal%d" % i, image_list[i]], ["#imageModal%d" % (i+1), image_list[i+1]], ["#imageModal%d" % (i+2), image_list[i+2]]])
        except Exception as e:
            # 报错说明, 爬取到的图片不足3 的倍数
            pass
    large_image = []
    for image in display_image:
        large_image += [[i[0].replace('#', ""), i[1]] for i in image]


    # print(large_image)
    return render_template('index.html', imagelist=display_image, large_image=large_image)


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('images/favicon.ico')

@app.route('/image/<num>')
def displayImage(num):
    # print(num)
    imageurllist = get_random_imageurl(int(num))
    return  render_template('images.html', imagelist=imageurllist)



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8999)
