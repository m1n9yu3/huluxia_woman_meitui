# crawling huluxia png

python3.7 environment
Using multithreading to optimize speed

Coding changes the world


![葫芦侠三楼](./src/葫芦侠三楼.jpg)

***The project is entertainment***

[简体中文](./src/zh_cn_README.md)

## Optimization log
2021.4.14:  Ready to delete multithreading, using faster asynchronous concurrency to achieve image capture

2021.4.26: Now I want to integrate the flash framework, browse the pictures on the web, and add a new picture address, Finished, code let me write waste, I can't understand anything, cry

2021.4.27:   The flash framework is finished, the page is not beautified, the logging module is added, and the log information is collected. There is only one simple function: localhost/image/number

2021.5.4:   After a glance, I found that I didn't upload GitHub at all, and the local modified code was gone. Can only change


## How to use?
install pip module
```shell
python -m pip install -r requirements.txt
```

bash run
```shell
python web_server.py
```

Browser input
http://127.0.0.1:8999/

Control the number of pictures
http://127.0.0.1:8999/image/100

LAN access, you can replace 127.0.0.1 cost machine IP address


![Alt text](./src/img/test.jpg)


## directory description

flask :
    
    -- static
    -- templates

tmp :   Store version iteration, old version file

src :   resource files




## If you want to develop with me, please contact me
m1n9yu3@foxmail.com