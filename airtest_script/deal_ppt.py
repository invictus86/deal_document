# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import win32api, json
import ctypes
import logging
import os
from airtest.core.api import *
from airtest.core.settings import Settings as ST
ST.CVSTRATEGY = ["tpl", "sift","brisk"]

logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                    filename='./log/auto_burn.log',
                    filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    # a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    # 日志格式
                    )

if not cli_setup():
    auto_setup(__file__, logdir=r"F:\code\get_baiduwenku\airtest_script\log", devices=[
        "Windows:///",
    ]
               )

# script content
print("start...")

# num = 15
for num in range(50):
    if num <= 22:
        continue
    list_file = os.listdir(r"F:\code\get_baiduwenku\xuekewang1\{}".format(num))
    print(list_file)
    for file_name in list_file[0:]:
        print(file_name)
        os.popen(r'F:\code\get_baiduwenku\xuekewang1\{}\{}'.format(num, file_name))
        # if list_file.index(file_name) == 0:
        print("打开ppt")
        time.sleep(3)
        if list_file.index(file_name) == 0:
            touch(Template(r"./images/ppt_sheji.png", threshold=0.90))
        else:
            pass

        try:
            touch(Template(r"./images/ppt_beijing.png", threshold=0.95))
        except:

            touch(Template(r"./images/ppt_sheji.png", threshold=0.90))
            touch(Template(r"./images/ppt_beijing.png", threshold=0.95))

        keyevent("{END}")
        try:
            touch(Template(r"./images/ppt_URL.png", threshold=0.90))
            time.sleep(0.5)
            keyevent("{DEL}")
        except:
            pass

        time.sleep(0.5)
        dev = device()

        # 拿到鼠标，并模拟鼠标的右键点击操作
        dev.mouse.right_click(coords=(916, 671))
        # dev.mouse.right_click(coords=(1046, 939))
        time.sleep(1)
        keyevent("{UP}")
        keyevent("{UP}")
        keyevent("{UP}")
        keyevent("{UP}")
        time.sleep(0.5)
        keyevent("{ENTER}")

        try:
            touch(Template(r"./images/ppt_yingyong.png", threshold=0.95))
        except:
            touch(Template(r"./images/ppt_beijing.png", threshold=0.95))
            touch(Template(r"./images/ppt_yingyong.png", threshold=0.95))

    touch(Template(r"./images/ppt_exit.png", threshold=0.95))
    time.sleep(1)
    dev = device()
    # 拿到鼠标，并模拟鼠标的右键点击操作
    dev.mouse.right_click(coords=(973, 510))
    # dev.mouse.right_click(coords=(1046, 939))
    # for _ in range(20):
    for _ in range(25):
        keyevent("{ENTER}")
        # touch(Template(r"./images/ppt_baocun.png", threshold=0.8))
        time.sleep(3)
