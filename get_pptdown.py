# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

import time
from selenium import webdriver
import json

ST.FIND_TIMEOUT = 30
from airtest.core.settings import Settings as ST

ST.CVSTRATEGY = ["tpl", "sift", "brisk"]


def read_json_file(file_path):
    """
    read json file from file path
    :param file_path:
    :return:
    """
    with open(file_path, 'r') as load_f:
        load_dict = json.load(load_f)
    return load_dict


def write_json_file(file_path, load_dict):
    """
    write json file from file path
    :param file_path:the path of file
    :param load_dict:dict data you want to write
    :return:
    """
    with open(file_path, "w") as dump_f:
        json.dump(load_dict, dump_f)


max_num = 7394

class Ppt(object):

    def __init__(self):
        self.url = 'https://www.ypppt.com/p/d.php?aid={}'
        self.path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

        options = webdriver.ChromeOptions()
        out_path = r'E:\yp_ppt'  # 是你想指定的路径
        prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': out_path}
        options.add_experimental_option('prefs', prefs)

        #         browser = webdriver.Chrome(executable_path=r'C:\Users\ivan.zhao\AppData\Local\Google\Chrome\Application\chromedriver.exe',
        #                            chrome_options=options)

        self.driver = webdriver.Chrome(executable_path=self.path, chrome_options=options)
        self.driver.implicitly_wait(10)  # seconds
        # self.file = open('ppt.json', 'w')

    def __del__(self):
        self.driver.close()
        # self.file.close()

    def run(self):
        # dict_data = read_json_file("F:\code\get_baiduwenku\cz_jiaoxie\jiaoxue_all.json")
        # list_data = dict_data.get("down_list")
        # start_num = 155057 + 1
        start_num = 702
        end_num = max_num + 1
        for i in range(start_num, end_num):
            print(i)
            try:
                self.driver.get((self.url).format(i))
                self.driver.find_elements_by_xpath('/html/body/div[2]/div/ul/li[1]/a')[0].click()
                time.sleep(2)
            except:
                print("异常了")
                print((self.url).format(i))

ppt = Ppt()
ppt.run()


