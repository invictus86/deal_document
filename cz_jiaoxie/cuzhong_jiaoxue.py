import json

import time
from selenium import webdriver

class Ppt(object):

    def __init__(self):
        self.url = 'http://cz.jb1000.com/Details/DownLoad.aspx?infoid={}'
        self.path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.driver.implicitly_wait(30)  # seconds
        self.file = open('ppt.json', 'w')

    def __del__(self):
        self.driver.close()
        self.file.close()

    def run(self):

        self.driver.get((self.url).format(1))
        time.sleep(2)

        self.driver.find_elements_by_xpath('//*[@id="txtusername"]')[0].send_keys('invictus')
        self.driver.find_elements_by_xpath('//*[@id="txtuserpass"]')[0].send_keys('invictus')
        self.driver.find_elements_by_xpath('//*[@id="btnLogin"]')[0].click()

        for i in range(733365):
            self.driver.get((self.url).format(i + 1))
            time.sleep(1)

            jinbi_element = self.driver.find_elements_by_xpath('//*[@id="pnlother"]/div[1]/div[2]/span[1]')[0]
            jinbi = jinbi_element.get_attribute("data-value")
            print(jinbi)

            if jinbi != "0":
                print("当前需要金币{}, 第{}次, 无法下载".format(jinbi, i))
                continue

            # time.sleep(2)
            self.driver.find_elements_by_xpath('//*[@id="infopointdownload"]')[0].click()
            print("当前第{}次, 可以下载".format(i))
            time.sleep(10)


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
