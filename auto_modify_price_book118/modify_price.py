# -*- encoding=utf8 -*-
__author__ = "Administrator"

import time
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from selenium import webdriver
import re
import os
import shutil

import win32api

if not cli_setup():
    auto_setup(__file__, devices=[
        "Windows:///",
    ]
               )

ST.FIND_TIMEOUT = 10
from airtest.core.settings import Settings as ST

ST.CVSTRATEGY = ["tpl", "sift", "brisk"]

# list_user_password = [
#     ["chaojida", "a1519517487"]
# ]
all_list_data = [
    ["chaojida1", "a1519517487"],
    ["chaojida2", "a1519517487"],
    ["chaojida3", "a1519517487"],
    ["chaojida4", "a1519517487"],
    ["chaojida5", "a1519517487"],
    ["chaojida6", "a1519517487"],
    ["chaojida7", "a1519517487"],
    ["chaojida8", "a1519517487"],
    ["chaojida9", "a1519517487"],
    ["chaojida10", "a1519517487"],
    ["chaojida11", "a1519517487"],
    ["chaojida12", "a1519517487"],
    ["chaojida13", "a1519517487"],
    ["chaojida14", "a1519517487"],
    ["chaojida15", "a1519517487"],
    ["chaojida16", "a1519517487"],
    ["chaojida17", "a1519517487"],
    ["chaojida18", "a1519517487"],
    ["chaojida19", "a1519517487"],
    ["chaojida20", "a1519517487"],
    ["chaojida21", "a1519517487"],
    ["chaojida22", "a1519517487"],
    ["chaojida23", "a1519517487"],
    ["chaojida24", "a1519517487"],
    ["chaojida25", "a1519517487"],
    ["chaojida26", "a1519517487"],
    ["chaojida27", "a1519517487"],
    ["chaojida28", "a1519517487"],
    ["chaojida29", "a1519517487"],
    ["chaojida30", "a1519517487"],
    ["chaojida31", "a1519517487"],
    ["chaojida32", "a1519517487"],
    ["chaojida33", "a1519517487"],
    ["chaojida34", "a1519517487"],
    ["chaojida35", "a1519517487"],
    ["chaojida36", "a1519517487"],
    ["chaojida37", "a1519517487"],
    ["chaojida38", "a1519517487"],
    ["chaojida39", "a1519517487"],
    ["chaojida40", "a1519517487"],
    ["chaojida41", "a1519517487"],
    ["chaojida42", "a1519517487"],
    ["chaojida43", "a1519517487"],
    ["chaojida44", "a1519517487"],
    ["chaojida45", "a1519517487"],
    ["chaojida46", "a1519517487"],
    ["chaojida47", "a1519517487"],
    ["chaojida48", "a1519517487"],
    ["chaojida49", "a1519517487"],
    ["chaojida50", "a1519517487"],
    ["chaojida51", "a1519517487"],
    ["chaojida52", "a1519517487"],
    ["chaojida53", "a1519517487"],
    ["chaojida54", "a1519517487"],
    ["chaojida55", "a1519517487"],
    ["chaojida56", "a1519517487"],
    ["chaojida57", "a1519517487"],
    ["chaojida58", "a1519517487"],
    ["chaojida59", "a1519517487"],
    ["chaojida60", "a1519517487"],

    ["chaojida1", "a1519517487"],
    ["chaojida2", "a1519517487"],
    ["chaojida3", "a1519517487"],
    ["chaojida4", "a1519517487"],
    ["chaojida5", "a1519517487"],
    ["chaojida6", "a1519517487"],
    ["chaojida7", "a1519517487"],
    ["chaojida8", "a1519517487"],
    ["chaojida9", "a1519517487"],
    ["chaojida10", "a1519517487"],
    ["chaojida11", "a1519517487"],
    ["chaojida12", "a1519517487"],
    ["chaojida13", "a1519517487"],
    ["chaojida14", "a1519517487"],
    ["chaojida15", "a1519517487"],
    ["chaojida16", "a1519517487"],
    ["chaojida17", "a1519517487"],
    ["chaojida18", "a1519517487"],
    ["chaojida19", "a1519517487"],
    ["chaojida20", "a1519517487"],
    ["chaojida21", "a1519517487"],
    ["chaojida22", "a1519517487"],
    ["chaojida23", "a1519517487"],
    ["chaojida24", "a1519517487"],
    ["chaojida25", "a1519517487"],
    ["chaojida26", "a1519517487"],
    ["chaojida27", "a1519517487"],
    ["chaojida28", "a1519517487"],
    ["chaojida29", "a1519517487"],
    ["chaojida30", "a1519517487"],
    ["chaojida31", "a1519517487"],
    ["chaojida32", "a1519517487"],
    ["chaojida33", "a1519517487"],
    ["chaojida34", "a1519517487"],
    ["chaojida35", "a1519517487"],
    ["chaojida36", "a1519517487"],
    ["chaojida37", "a1519517487"],
    ["chaojida38", "a1519517487"],
    ["chaojida39", "a1519517487"],
    ["chaojida40", "a1519517487"],
    ["chaojida41", "a1519517487"],
    ["chaojida42", "a1519517487"],
    ["chaojida43", "a1519517487"],
    ["chaojida44", "a1519517487"],
    ["chaojida45", "a1519517487"],
    ["chaojida46", "a1519517487"],
    ["chaojida47", "a1519517487"],
    ["chaojida48", "a1519517487"],
    ["chaojida49", "a1519517487"],
    ["chaojida50", "a1519517487"],
    ["chaojida51", "a1519517487"],
    ["chaojida52", "a1519517487"],
    ["chaojida53", "a1519517487"],
    ["chaojida54", "a1519517487"],
    ["chaojida55", "a1519517487"],
    ["chaojida56", "a1519517487"],
    ["chaojida57", "a1519517487"],
    ["chaojida58", "a1519517487"],
    ["chaojida59", "a1519517487"],
    ["chaojida60", "a1519517487"],
]

with open("./2021-09-26-14-33-01-0.txt", "r") as f:
    word_list = f.readlines()


def del_all_file(filepath):
    """
    删除某一目录下的所有文件与文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


class Ppt(object):

    def __init__(self):
        self.url = 'https://max.book118.com/'
        self.path = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
        # self.file = open('ppt.json', 'w')

    def __del__(self):
        self.driver.close()

    def run_drive(self):
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'E:\原创力下载\\'}
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(executable_path=self.path, options=options)
        self.driver.implicitly_wait(3)  # seconds

    def run(self):
        word_num = -1
        for word in word_list[6140:]:
            word_num = word_num + 1
            num_index = word_num % 60
            list_data = all_list_data[num_index]
            try:
                print(list_data)
                self.run_drive()
                self.driver.get(self.url)
                time.sleep(0.5)

                self.driver.find_element_by_xpath('//*[@id="header"]/div/ul[2]/li[5]/a').click()
                self.driver.switch_to.frame("layui-layer-iframe1")

                self.driver.find_element_by_class_name('login-account').click()

                self.driver.find_element_by_xpath(
                    '//*[@id="main"]/div/div/div[3]/dl/dd[1]/form/div[1]/p[1]/input').send_keys(
                    list_data[0])
                self.driver.find_element_by_xpath(
                    '//*[@id="main"]/div/div/div[3]/dl/dd[1]/form/div[2]/p[1]/input[2]').send_keys(list_data[1])
                self.driver.find_element_by_xpath(
                    '//*[@id="main"]/div/div/div[3]/dl/dd[1]/form/div[4]/p[1]/input').click()

                print(word)
                print(word_list.index(word))

                time.sleep(5)
                handles = self.driver.window_handles
                self.driver.switch_to.window(handles[0])
                time.sleep(0.5)
                # 文档主页
                try:
                    self.driver.get("https://max.book118.com/search.html?page=1&q={}&doc_type=3".format(word))
                except:
                    handles = self.driver.window_handles
                    self.driver.switch_to.window(handles[0])
                    self.driver.close()
                    continue
                time.sleep(2)

                # 获取页数
                try:
                    page_num = self.driver.find_elements_by_xpath('//*[@id="main"]/div[1]/div[2]/div[2]/div')[0].text
                    page = re.findall("共(.*?)页", page_num)[0]
                    print(page)
                except:
                    handles = self.driver.window_handles
                    self.driver.switch_to.window(handles[0])
                    self.driver.close()
                    continue

                if int(page) == 0:
                    continue
                for i in range(int(page)):
                    handles = self.driver.window_handles
                    self.driver.switch_to.window(handles[0])
                    time.sleep(0.5)

                    self.driver.get(
                        "https://max.book118.com/search.html?page={}&q={}&doc_type=3".format(i + 1, word))
                    file_url_list = self.driver.find_elements_by_xpath('//*[@id="main"]/div[1]/div[2]/ul/li/div[2]/a')
                    for file_url in file_url_list:
                        handles = self.driver.window_handles
                        self.driver.switch_to.window(handles[0])

                        file_url.click()
                        time.sleep(5)
                        handles = self.driver.window_handles
                        self.driver.switch_to.window(handles[1])

                        down_file_name = self.driver.find_elements_by_xpath('//*[@id="main"]/div[1]/div[1]/h1')[0].text
                        print(down_file_name)
                        try:
                            self.driver.find_element_by_xpath('//*[@id="title_download"]').click()
                        except:
                            self.driver.close()
                            continue

                        try:
                            touch(Template(r"./tpl1634366031228.png", threshold=0.9))
                            time.sleep(5)
                            list_file = os.listdir("E:\原创力下载")
                            if len(list_file) >= 2:
                                del_all_file("E:\原创力下载")
                                continue
                            elif len(list_file) == 0:
                                continue
                            else:

                                for i in range(20):
                                    list_file = os.listdir("E:\原创力下载")
                                    file_name = list_file[0]
                                    if file_name[-11:] == ".crdownload":
                                        time.sleep(3)
                                    else:
                                        pass
                                    # del_all_file("E:\原创力下载")
                                list_file = os.listdir("E:\原创力下载")
                                file_name = list_file[0]
                                if file_name[-11:] == ".crdownload":
                                    del_all_file("E:\原创力下载")
                                    continue
                                shutil.move("E:\原创力下载\{}".format(file_name), "E:\原创力下载成功\{}".format(down_file_name))
                        except:
                            pass
                        finally:
                            self.driver.close()
                        time.sleep(1)
                    time.sleep(3)
            except:
                handles = self.driver.window_handles
                self.driver.switch_to.window(handles[0])
                self.driver.close()
                time.sleep(3)
                continue
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[0])
            self.driver.close()
            time.sleep(3)


ppt = Ppt()
ppt.run()
