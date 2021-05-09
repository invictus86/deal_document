import json

import time
from selenium import webdriver


def write_json_file(file_path, load_dict):
    with open(file_path, "w") as dump_f:
        json.dump(load_dict, dump_f)


class Ppt(object):

    def __init__(self):
        self.url = 'https://yw.zxxk.com/p/books-type1/index-{}.html?level=1'
        self.path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.driver.implicitly_wait(30)  # seconds
        self.file = open('ppt.json', 'w')

    def save_data(self, data_list):
        for data in data_list:
            print(data)
            json_data = json.dumps(data, ensure_ascii=False) + ',\n'
            self.file.write(json_data)

    def __del__(self):
        self.driver.close()
        self.file.close()

    def run(self):
        self.driver.get((self.url).format("1"))
        try:
            self.driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div/div[2]/a')[0].click()
        except:
            pass
        time.sleep(2)
        self.driver.find_elements_by_xpath('//*[@id="un-login"]/a[1]')[0].click()
        # /html/body/div[2]/div[2]/div/div[2]/a
        time.sleep(30)

        # 小学语文配置 勿删除
        # with open("./xuekewang1.json", "r") as load_f:
        #     load_dict = json.load(load_f)
        # list_url = load_dict.get("yuwen_kejian")
        # # list_url = load_dict
        # # list_url = list_url[198:398]
        # list_url = list_url[2398:2598]

        # # 高中拓展配置
        # with open("./gaozhong_tuozhan.json", "r") as load_f:
        #     load_dict = json.load(load_f)
        # list_url = load_dict.get("gaozhong_tuozhan")

        # 小学综合实践
        with open("./xiaoxue_zongheshijian.json", "r") as load_f:
            load_dict = json.load(load_f)
        list_url = load_dict.get("xiaoxue_zongheshijian")

        # 高中已经爬取120篇
        # list_url = list_url[120:200]

        list_url = list_url[200:400]

        for url in list_url:
            try:
                self.driver.get(url)
                time.sleep(2)
                print(url)
                print(list_url.index(url))
                down_ico = self.driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div[2]')[0]
                down_ico.click()
                print(down_ico)

                # down_ico1 = self.driver.find_elements_by_xpath('/html/body/div[11]/div[2]/div[3]/div[1]/a')[0]
                # down_ico1.click()

                time.sleep(2)
            except:
                continue


if __name__ == '__main__':
    ppt = Ppt()
    ppt.run()
