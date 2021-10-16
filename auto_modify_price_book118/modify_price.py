# -*- encoding=utf8 -*-
__author__ = "Administrator"

# from airtest.core.api import *
#
# auto_setup(__file__)

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

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
    # ["zy_mi", "zfj6245xyz"],
    # ["yajiujin123", "yajiujin123"],
    # ["18873466719", "liu123aaa"],
    # ["17770994504", "popo1127"],
    # ["4-16weizifu", "nb666888"],
    # ["18664323478", "yhbs199401"],
    # ["16312752265bc36", "hxg202109"],
    # ["1630940552a1f3f", "lsf445477"],
    # ["13827279166", "anny123456"],
    # ["330312164", "dong6251988"],
    # ["Lanhong6152", "Lanhong5617"],
    # ["YYL520", "520yangqiuling"],
    # ["13421840026", "zqy768023"],


    ["15817398255", "a1519517487"],
    ["18824632883", "a1519517487"],
    ["kuaileketang", "a1519517487"],
    ["yimoxieyang", "a1519517487"]
]
# username = "15817398255"
# password = "a1519517487"


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
        self.driver.implicitly_wait(3)  # seconds

    def run(self):
        for list_data in list_user_password:
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

                # 关闭自审提示
                try:
                    self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]/div/div/a[3]').click()
                    time.sleep(0.5)
                except:
                    pass

                self.driver.switch_to.frame("doc_index_iframe")
                time.sleep(0.5)
                # 点击普通文档
                self.driver.find_element_by_xpath('//*[@id="filter_mold"]/ul/li[2]/a').click()
                time.sleep(0.5)
                # 点击页数排序
                self.driver.find_element_by_xpath('//*[@id="sort"]/div/ul/li[5]/a').click()
                time.sleep(0.5)
                self.driver.find_element_by_xpath('//*[@id="sort"]/div/ul/li[5]/a').click()
                time.sleep(0.5)

                self.driver.find_element_by_xpath('//*[@id="filter_toggle"]/a[1]/span').click()
                time.sleep(0.5)
                self.driver.find_element_by_xpath('//*[@id="filter_page"]/ul/li[2]/a').click()
                time.sleep(0.5)

                for data in ['//*[@id="filter_format"]/ul[1]/li[2]/a', '//*[@id="filter_format"]/ul[1]/li[3]/a',
                             '//*[@id="filter_format"]/ul[1]/li[6]/a']:
                # for data in ['//*[@id="filter_format"]/ul[1]/li[6]/a']:

                    try:
                        self.driver.find_element_by_xpath(data).click()
                        time.sleep(0.5)

                        all_num = self.driver.find_element_by_xpath('//*[@id="paging"]/div/div[1]/strong').text
                        print("总数： {}".format(all_num))
                        page_num = int(all_num) // 50 + 1
                        print("页数： {}".format(page_num))

                        for i in range(page_num):
                            first_num = int(
                                self.driver.find_element_by_xpath(
                                    '//*[@id="table"]/div[1]/table/tbody/tr[1]/td[9]').text)
                            print(i)
                            print(first_num)
                            if first_num >= 30:
                                nex_page = i + 1
                                # nex_page = i + 50
                                # print(nex_page)
                                self.driver.find_element_by_xpath('//*[@id="d_page_num"]').send_keys(Keys.CONTROL + "a")
                                self.driver.find_element_by_xpath('//*[@id="d_page_num"]').send_keys(Keys.DELETE)
                                self.driver.find_element_by_xpath('//*[@id="d_page_num"]').send_keys(str(nex_page))
                                time.sleep(0.5)
                                self.driver.find_element_by_xpath('//*[@id="paging"]/div/div[2]/span[3]').click()
                                time.sleep(0.5)
                            elif 2 <= first_num < 30:
                                # 点击全选
                                self.driver.find_element_by_xpath('//*[@id="batch"]/div/div[1]/label/i').click()
                                time.sleep(0.5)
                                # 点击批量修改
                                self.driver.find_element_by_xpath('//*[@id="batch"]/div/div[2]/a[1]').click()
                                time.sleep(0.5)
                                self.driver.switch_to.frame("layui-layer-iframe1")
                                time.sleep(0.5)
                                # 点击普通不适合全文阅读
                                try:
                                    self.driver.find_element_by_xpath('//*[@id="type"]/label[5]/i').click()
                                except:
                                    self.driver.find_element_by_xpath('//*[@id="type"]/label[3]/i').click()
                                time.sleep(0.5)
                                # 输入免费页数
                                if 20 < first_num < 30:
                                    self.driver.find_element_by_xpath('//*[@id="read"]').send_keys("10")
                                    time.sleep(0.5)
                                    self.driver.find_element_by_xpath('//*[@id="page"]').send_keys("35")
                                elif 10 <= first_num <= 20:
                                    self.driver.find_element_by_xpath('//*[@id="read"]').send_keys("7")
                                    time.sleep(0.5)
                                    self.driver.find_element_by_xpath('//*[@id="page"]').send_keys("30")
                                elif 5 < first_num < 10:
                                    self.driver.find_element_by_xpath('//*[@id="read"]').send_keys("4")
                                    time.sleep(0.5)
                                    self.driver.find_element_by_xpath('//*[@id="page"]').send_keys("20")
                                elif 4 <= first_num <= 5:
                                    self.driver.find_element_by_xpath('//*[@id="read"]').send_keys("3")
                                    time.sleep(0.5)
                                    self.driver.find_element_by_xpath('//*[@id="page"]').send_keys("10")
                                elif first_num == 3:
                                    self.driver.find_element_by_xpath('//*[@id="read"]').send_keys("2")
                                    time.sleep(0.5)
                                    self.driver.find_element_by_xpath('//*[@id="page"]').send_keys("10")
                                elif first_num == 2:
                                    self.driver.find_element_by_xpath('//*[@id="read"]').send_keys("1")
                                    time.sleep(0.5)
                                    self.driver.find_element_by_xpath('//*[@id="page"]').send_keys("10")
                                time.sleep(0.5)
                                self.driver.find_element_by_xpath('//*[@id="edit_btn_sub"]').click()
                                # time.sleep(10)
                                time.sleep(5)
                                self.driver.switch_to.default_content()
                                # self.driver.switch_to.frame(0)
                                self.driver.switch_to.frame("doc_index_iframe")

                            else:
                                # print("当前文档页数为: " + str(first_num))
                                print("结束改价")
                                break
                    except:
                        continue
            except:
                self.driver.close()
                time.sleep(3)
                continue
            self.driver.close()
            time.sleep(3)


ppt = Ppt()
ppt.run()
