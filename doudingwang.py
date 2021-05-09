import json

import time
from selenium import webdriver
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


class Ppt(object):

    def __init__(self):
        self.url = 'https://www.docin.com/l-10008-0-0-0-4-{}.html'
        self.path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.driver.implicitly_wait(30)  # seconds
        self.file = open('ppt.json', 'w')

    def parse_data(self):

        # down_ico = self.driver.find_elements_by_xpath('//*[@id="btnSoftDownload"]')
        # down_ico.click()

        # 获取房间列表
        # next_ico = self.driver.find_element_by_class_name('nextPage xh-highlight')
        # next_ico.click()

        ppt_list = self.driver.find_elements_by_xpath('//*[@id="showStyle"]/div[4]/dl/dd/a')
        # print(ppt_list)
        # /html/body/div[3]/div[2]/div[2]/div[3]//div/a
        # //*[@id="4048888"]/div[1]/a
        print(len(ppt_list))
        # print(ppt_list)
        # href_list = self.driver.find_elements_by_xpath('/html/body/div[6]/dl/dd/ul/li/h2/a/@href')
        # image_list = self.driver.find_elements_by_xpath('/html/body/div[6]/dl/dd/ul/li/a/img')
        # name_list = self.driver.find_elements_by_xpath('/html/body/div[6]/dl/dd/ul/li/h2/a')
        # print(len(houses_list))
        data_list = []
        # 遍历节点列表
        for ppt in ppt_list:
            ppt_href = ppt.get_attribute('href')
            print(ppt_href)
            data_list.append(ppt_href)
            # js = 'window.open({}});'.format(ppt_href)  # 通过执行js，开启一个新的窗口
            # self.driver.execute_script(js)
            # # self.driver.get(ppt_href)
            # # ppt.click()
            # time.sleep(1)
            # self.driver.switch_to.window(self.driver.window_handles[-1])
            # # self.driver.close()
            # down_ico = self.driver.find_elements_by_xpath('//*[@id="btnSoftDownload"]')
            # down_ico.click()
            # time.sleep(1)
            #
            # # self.driver.switch_to.window(self.driver.window_handles[-1])
            # self.driver.close()
            #
            # # self.driver.switch_to.window(self.driver.window_handles[-1])
            # # self.driver.close()
            # self.driver.switch_to.window(self.driver.window_handles[-1])
            # time.sleep(1)
            # if (ppt_list.index(ppt) + 1) % 14 == 0:
            #     next_ico = self.driver.find_element_by_xpath('//*[@id="mainBox"]/div/div/div/span[9]')
            #     next_ico.click()
        return data_list

    def save_data(self, data_list):
        for data in data_list:
            print(data)
            json_data = json.dumps(data, ensure_ascii=False) + ',\n'
            self.file.write(json_data)

    def __del__(self):
        self.driver.close()
        self.file.close()

    def run(self):
        # 开启循环
        # 构建url
        # 发送请求
        self.driver.get((self.url).format("1"))
        # time.sleep(20)
        # try:
        #     self.driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div/div[2]/a')[0].click()
        # except:
        #     pass
        # time.sleep(2)
        # self.driver.find_elements_by_xpath('//*[@id="un-login"]/a[1]')[0].click()
        # # /html/body/div[2]/div[2]/div/div[2]/a
        # time.sleep(30)
        #
        # with open("./xuekewang1.json", "r") as load_f:
        #     load_dict = json.load(load_f)
        # list_url = load_dict.get("yuwen_kejian")
        # # list_url = load_dict
        # # list_url = list_url[198:398]
        # list_url = list_url[998:1198]
        # for url in list_url:
        #     # try:
        #     self.driver.get(url)
        #     # down_ico = self.driver.find_elements_by_xpath('//*[@id="btnSoftDownload"]')[0]
        #     # down_ico.click()
        #     time.sleep(2)
        #     print(url)
        #     print(list_url.index(url))
        #     down_ico = self.driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div[2]')[0]
        #     # down_ico = self.driver.find_elements_by_xpath('//*[@id="btnSoftDownload"]/div')[0]
        #     down_ico.click()
        #     print(down_ico)
        #     time.sleep(2)
        #     # except:
        #     #     continue
        #     #     print()

        data_list = self.parse_data()
        print(data_list)
        with open("111.used_txt", "a") as f:
            for href in data_list:
                f.write(href + "\r")
        # # list_all = []
        #     self.driver.get((self.url).format("1"))
        # # time.sleep(20)
        # self.driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div/div[2]/a')[0].click()
        # for i in range(400):
        #     self.driver.get((self.url).format(i))
        #     # self.driver.find_elements_by_xpath('//*[@id="un-login"]/a[1]')[0].click()
        #     # /html/body/div[2]/div[2]/div/div[2]/a
        #     # time.sleep(20)
        #
        #     data_list = self.parse_data()
        #     list_all = list_all + data_list
        #     print(list_all)
        #
        # dict_data = {"uywen_kejian": list_all}
        # write_json_file("./xuekewang.json", dict_data)

        # for i in range(152):
        # # for i in range(2):
        #     if i == 0:
        #         self.driver.get("http://www.1ppt.com/moban/")
        #     else:
        #         self.driver.get(self.url.format(str(i + 1)))
        #     # while True:
        #     # 解析数据，页面元素定位，使用xpath
        #     data_list = self.parse_data()
        #     # 保存数据
        #     self.save_data(data_list)


if __name__ == '__main__':
    ppt = Ppt()
    ppt.run()

    # with open("./xuekewang.json", "r") as load_f:
    #     load_dict = json.load(load_f)
    #
    #     list_data = load_dict.get("uywen_kejian")
    #     print(len(list_data))
    #     new_list = list(set(list_data))
    #     print(len(new_list))
    #
    # new_dict = {"yuwen_kejian": new_list}
    # write_json_file("./xuekewang1.json", new_list)
