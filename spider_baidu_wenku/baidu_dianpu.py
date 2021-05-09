import json

import time
from selenium import webdriver
import requests
import random
import os
from selenium.webdriver.support.ui import Select
from test_code import download_ppt


# 需求：爬取斗鱼直播的房间信息，title、type、owner、num、cover

# 流程：
# 开启循环
# 构建url
# 发送请求
# 解析数据，页面元素定位，使用xpath
# 保存数据
# 下一页定位，有循环终止条件

def write_json_file(file_path, load_dict):
    with open(file_path, "w") as dump_f:
        json.dump(load_dict, dump_f)


def read_json_file(file_path):
    """
    read json file from file path
    :param file_path:
    :return:
    """
    with open(file_path, 'r') as load_f:
        load_dict = json.load(load_f)
    return load_dict

with open("./baidu_dianpu.txt", "r") as f:
    list_url = f.readlines()
# print(list_url)


class Ppt(object):

    def __init__(self):
        # self.url = 'https://wenku.baidu.com/ndcore/browse/sub?isBus=2&isPus=3&isChild=&isType=0'
        self.path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.driver.implicitly_wait(15)  # seconds

    def __del__(self):
        self.driver.close()

    def run(self):
        # 开启循环
        # 构建url
        # 发送请求
        transfer_list_url = []
        for url in list_url:
            print(list_url.index(url))

            self.driver.get(url)
            current_url = self.driver.current_url
            print(current_url)
            transfer_list_url.append(current_url)
            # time.sleep(15)
        with open("./transfer_url.txt", "a") as f:
            for transfer_url in transfer_list_url:
                f.write(transfer_url + "\n")
            # time.sleep(1000000)

            # dianpu_list = self.driver.find_elements_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div[1]/div[2]/div[3]/ul/li/div[2]/a/@href')
            # print(dianpu_list)
            # try:
            #     self.driver.find_elements_by_xpath('/html/body/div/div/div[2]/div[2]')[0].click()
            # except:
            #     pass
            # # 点击文档
            # self.driver.find_elements_by_xpath('//*[@id="app"]/div/aside/ul/li[2]/ul/li/ul/li[1]')[0].click()
            # # 点击vip文档
            # # self.driver.find_elements_by_xpath('//*[@id="app"]/section/main/div[1]/div/div[1]/div[1]/div[1]')[0].click()
            # # self.driver.find_elements_by_xpath('/html/body/div/div[1]/div[1]/ul/li[4]')[0].click()
            # print("输入")
            # time.sleep(10)
            #
            # # 点击其他
            # # s1 = Select(self.driver.find_elements_by_xpath('//*[@id="app"]/section/main/div[1]/div/div[1]/div[2]/div[3]/div/span/span/i'))       # 实例化Select
            # # s1.select_by_index(3)
            #
            # list_data = []
            # # for i in range(38):
            # for i in range(236):
            #     id_list = self.driver.find_elements_by_xpath(
            #         '//*[@id="app"]/section/main/div[1]/div/div[1]/div[4]/div[3]/table/tbody/tr/td[5]/div/span[2]')
            #     # id_list = self.driver.find_elements_by_xpath(
            #     #     '//*[@id="app"]/section/main/div[1]/div/div[1]/div[4]/div[3]/table/tbody/tr/td[6]/div/span[2]')
            #     for id in id_list:
            #         print(id.get_attribute("data-clipboard-text"))
            #         list_data.append(id.get_attribute("data-clipboard-text"))
            #     self.driver.find_elements_by_xpath('//*[@id="app"]/section/main/div[1]/div/div[1]/div[5]/div/button[2]')[
            #         0].click()
            #     print(i)
            #     time.sleep(0.5)
            # write_json_file("./baidu_no_update_fufe2.json", {"baidu_no_update": list_data})
            #
            # time.sleep(2)


if __name__ == '__main__':
    ppt = Ppt()
    ppt.run()



