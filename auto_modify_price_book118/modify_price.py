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
list_data = ["chaojida1", "a1519517487"]

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
        for word in word_list[47:]:
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

                time.sleep(10)
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
