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


dict_err = read_json_file("F:\code\get_baiduwenku\cz_jiaoxie\down_err.json")
# print(dict_data)
list_err = dict_err.get("down_err")
print(list_err)


class Ppt(object):

    def __init__(self):
        self.url = 'http://cz.jb1000.com/Details/DownLoad.aspx?infoid={}'
        self.path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

        options = webdriver.ChromeOptions()
        out_path = r'E:\google_download'  # 是你想指定的路径
        prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': out_path}
        options.add_experimental_option('prefs', prefs)

        #         browser = webdriver.Chrome(executable_path=r'C:\Users\ivan.zhao\AppData\Local\Google\Chrome\Application\chromedriver.exe',
        #                            chrome_options=options)

        self.driver = webdriver.Chrome(executable_path=self.path, chrome_options=options)
        self.driver.implicitly_wait(30)  # seconds
        self.file = open('ppt.json', 'w')

    def __del__(self):
        self.driver.close()
        self.file.close()

    def run(self):
        dict_data = read_json_file("F:\code\get_baiduwenku\cz_jiaoxie\jiaoxue_all.json")
        list_data = dict_data.get("down_list")

        self.driver.get((self.url).format(1))
        time.sleep(2)

        self.driver.find_elements_by_xpath('//*[@id="txtusername"]')[0].send_keys('invictus')
        self.driver.find_elements_by_xpath('//*[@id="txtuserpass"]')[0].send_keys('invictus')
        self.driver.find_elements_by_xpath('//*[@id="btnLogin"]')[0].click()

        #         start_num = 733365
        #         start_num = 731180

        #         for data in list_data[31:]:
        #         for data in list_data[86671:200000]:
        for data in list_data[91370:200000]:

            index_data = list_data.index(data)
            i = data[0]

            try:
                self.driver.get((self.url).format("496213"))
                time.sleep(1)

                #                 jinbi_element = self.driver.find_elements_by_xpath('//*[@id="pnlother"]/div[1]/div[2]/span[1]')[0]
                #                 jinbi = jinbi_element.get_attribute("data-value")
                #                 print(jinbi)

                #                 if jinbi != "0":
                #                     print("当前需要金币{}, 第{}次, 无法下载".format(jinbi, start_num - i))
                #                     continue

                #                 time.sleep(1)
                #                 print("当前第{}次, 可以下载".format(start_num - i))
                # self.driver.find_elements_by_xpath('//*[@id="infopointdownload"]')[0].click()
                elements = self.driver.find_elements_by_xpath('//*[@id="infopointdownload"]')[0]  # 再次获取元素，预防StaleElementReferenceException
                self.driver.execute_script('arguments[0].click();', elements)  # 模拟用户点击

                # try:
                #     touch(Template(r"tpl1613485730879.png", record_pos=(-0.261, -0.114), resolution=(3286, 1080)))
                #     data[1] = "pass"
                #     print("index_data : {} 下载成功".format(index_data))
                # except:
                #     touch(Template(r"tpl1613485730879.png", record_pos=(-0.261, -0.114), resolution=(3286, 1080)))
                #     data[1] = "pass"
                #     print("index_data : {} 下载成功".format(index_data))
                # #                 time.sleep(2)
                time.sleep(1)
            except:
                pass
                # print("index_data : {} 出现异常".format(index_data))
                # list_err.append(data)
                # write_json_file("F:\code\get_baiduwenku\cz_jiaoxie\down_err.json", {"down_err": list_err})


#             if index_data % 20== 0:
#                 write_json_file("./jiaoxue_all.json", {"down_list": list_data})


ppt = Ppt()
ppt.run()
