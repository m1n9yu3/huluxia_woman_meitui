# 爬取葫芦侠小姐姐 图片

python3.7 环境
使用多线程优化速度

编程改变世界

![葫芦侠三楼](./src/葫芦侠三楼.jpg)

***该项目属娱乐***

## 优化日志
2021.4.14:  准备删掉多线程 ， 使用更快的异步并发来实现图片抓取


2021.4.26:  异步计划泡汤，现在想整成 flask 框架， 网页浏览图片， 美滋滋, 新增获取 图片 地址,
    完了，代码让我写废了， 我啥都看不懂了， 哭了，呜呜呜·


2021.4.27:   flask 框架整好了， 差点页面美化， 增加了logging 模块， 日志信息收集， 只有一个简单的功能， localhost/image/图片数量 

2021.5.4:   瞅了一眼，发现，我根本没有上传 github, 而本地改过的代码也没了。 只能重新改...


## 如何使用
安装模块
```shell
python -m pip install -r requirements.txt
```

命令行输入
bash run
```shell
python web_server.py
```

浏览器输入 
http://127.0.0.1:8999/

控制图片数量
http://127.0.0.1:8999/image/100

局域网访问，可以将 127.0.0.1 替换成 本机ip地址

[comment]: <> (![test]&#40;&#41;)

![Alt text](./src/img/test.jpg)


## 目录说明

flask 目录:
    
    -- static
    -- templates

tmp :   存放版本迭代，老版本的文件

src :   存放资源文件




## 有一起开发的想法 可以联系我
m1n9yu3@foxmail.com