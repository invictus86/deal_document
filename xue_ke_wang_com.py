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
        # self.url = 'https://yw.zxxk.com/p/books-type1/index-{}.html?level=1'

        # gaozhong tuozhan
        # self.url = 'https://tz.zxxk.com/h/books/index-{}.html?level=1&order=viewhits_desc'
        self.url = 'https://zhsj.zxxk.com/p/books/index-{}.html?level=1&order=viewhits'
        self.path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.driver.implicitly_wait(20)  # seconds
        # self.file = open('ppt.json', 'w')

    def parse_data(self):
        # 获取房间列表
        # next_ico = self.driver.find_element_by_class_name('nextPage xh-highlight')
        # next_ico.click()

        ppt_list = self.driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div[2]/div[3]/div/div[1]/a')
        # print(ppt_list)
        # /html/body/div[3]/div[2]/div[2]/div[3]//div/a
        # //*[@id="4048888"]/div[1]/a
        print(len(ppt_list))

        data_list = []
        # 遍历节点列表
        for ppt in ppt_list:
            ppt_href = ppt.get_attribute('href')
            data_list.append(ppt_href)

        return data_list


    def __del__(self):
        self.driver.close()
        # self.file.close()

    def run(self):
        # 开启循环
        # 构建url
        # 发送请求
        list_all = []
        self.driver.get((self.url).format("1"))
        # time.sleep(20)
        self.driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div/div[2]/a')[0].click()
        # for i in range(400):
        for i in range(140):
            self.driver.get((self.url).format(i))

            data_list = self.parse_data()
            list_all = list_all + data_list
            print(list_all)

        dict_data = {"xiaoxue_zongheshijian": list_all}
        write_json_file("./xiaoxue_zongheshijian.json", dict_data)


if __name__ == '__main__':
    # ppt = Ppt()
    # ppt.run()

    with open("./xiaoxue_zongheshijian.json", "r") as load_f:
        load_dict = json.load(load_f)

        list_data = load_dict.get("xiaoxue_zongheshijian")
        print(len(list_data))
        new_list = list(set(list_data))
        print(len(new_list))

    new_dict = {"xiaoxue_zongheshijian": new_list}
    write_json_file("./xiaoxue_zongheshijian.json", new_dict)
