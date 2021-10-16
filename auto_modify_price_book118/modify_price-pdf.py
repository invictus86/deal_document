# -*- encoding=utf8 -*-
__author__ = "Administrator"

# from airtest.core.api import *
#
# auto_setup(__file__)

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
from selenium.webdriver import ActionChains


def write_json_file(file_path, load_dict):
    """
    write json file from file path
    :param file_path:the path of file
    :param load_dict:dict data you want to write
    :return:
    """
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

# username = "15817398255"
# password = "a1519517487"
list_user_password = [
    # ["18200710512", "a1519517487"],
    # ["15889319301", "popo1127"],
    # ["13545453704", "a1519517487"],
    # ["15971215297", "a1519517487"],
    # ["13733493604", "a1519517487"],
    # ["15919813673", "Justdoit2"],
    # ["15116809602", "popo1127"],
    # ["13627093316", "a1519517487"],
    # ["13799070036", "a1519517487"],
    # ["13267035182", "qwer@1234!"],
    ["15817398255", "a1519517487"],
    ["18824632883", "a1519517487"],
    ["kuaileketang", "a1519517487"],
    ["yimoxieyang", "a1519517487"]
]


# ["15817398255", "a1519517487"],
# ["18824632883", "a1519517487"],
# ["kuaileketang", "a1519517487"]]


class Ppt(object):

    def __init__(self):
        self.url = 'https://max.book118.com/'
        self.path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

        # self.file = open('ppt.json', 'w')

    def __del__(self):
        self.driver.close()

    def run_drive(self):
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.driver.implicitly_wait(15)  # seconds

    def run(self):
        for list_data in list_user_password:
            all_url_title_page = {}
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

                time.sleep(2)
                # # 进入发布成功文档
                self.driver.get("https://max.book118.com/user_center_v1/doc/index/index.html#audited")

                time.sleep(3)

                self.driver.switch_to.frame("doc_index_iframe")
                time.sleep(0.5)
                # # 点击pdf文档
                # self.driver.find_element_by_xpath('//*[@id="filter_mold"]/ul/li[2]/a').click()
                # time.sleep(0.5)
                # 点击页数排序
                self.driver.find_element_by_xpath('//*[@id="sort"]/div/ul/li[5]/a').click()
                time.sleep(0.5)
                self.driver.find_element_by_xpath('//*[@id="sort"]/div/ul/li[5]/a').click()
                time.sleep(0.5)

                # self.driver.find_element_by_xpath('//*[@id="filter_toggle"]/a[1]/span').click()
                # time.sleep(0.5)
                # self.driver.find_element_by_xpath('//*[@id="filter_page"]/ul/li[2]/a').click()
                # time.sleep(0.5)

                for data in ['//*[@id="filter_format"]/ul[1]/li[6]/a']:
                    # try:
                    self.driver.find_element_by_xpath(data).click()
                    time.sleep(0.5)

                    all_num = self.driver.find_element_by_xpath('//*[@id="paging"]/div/div[1]/strong').text
                    print(all_num)
                    page_num = int(all_num) // 50
                    print(page_num)

                    for i in range(page_num):
                        # self.driver.find_elements_by_xpath()
                        list_title = self.driver.find_elements_by_xpath('//*[@id="table"]/div[1]/table/tbody/tr/td[3]/a')
                        list_page = self.driver.find_elements_by_xpath('//*[@id="table"]/div[1]/table/tbody/tr/td[9]')
                        print(i)
                        # print(list_title)
                        for num in range(len(list_title)):
                            title = list_title[num].text
                            page = list_page[num].text
                            print(title)
                            print(page)
                            all_url_title_page.update({title: page})
                            # print(all_url_title_page)
                        try:
                            write_json_file("./{}.json".format(list_data[0]), all_url_title_page)
                        except:
                            print("写json失败")
                        nex_page = i + 2

                        time.sleep(0.5)
                        self.driver.find_element_by_xpath('//*[@id="d_page_num"]').send_keys(Keys.CONTROL + "a")
                        time.sleep(0.5)
                        self.driver.find_element_by_xpath('//*[@id="d_page_num"]').send_keys(Keys.DELETE)
                        time.sleep(0.5)
                        self.driver.find_element_by_xpath('//*[@id="d_page_num"]').send_keys(str(nex_page))
                        time.sleep(0.5)
                        self.driver.find_element_by_xpath('//*[@id="paging"]/div/div[2]/span[3]').click()
                        time.sleep(0.5)

                        # except:
                        #     continue
            except:
                self.driver.close()
                time.sleep(3)
                continue
            self.driver.close()
            time.sleep(3)


ppt = Ppt()
ppt.run()

# data = read_json_file("./15889319301.json")
# print(data)