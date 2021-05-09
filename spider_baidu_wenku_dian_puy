import json

import time
from selenium import webdriver
import requests
import random
import os
from selenium.webdriver.support.ui import Select
from test_code import download_ppt



if __name__ == '__main__':
    # ppt = Ppt()
    # ppt.run()

    with open(r"D:\My Documents\Tencent Files\1519517487\FileRecv\不登陆连接采集软件\result\invictus71_4956000538.txt") as f:
        all_list = f.readlines()
    # print(all_list)
    # all_list = all_list.reverse()
    print(all_list)
    print(len(all_list))

    headers = {
        # 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }

    for data in all_list[::-1]:
        url = data.replace("\n", "")
        print(url)
        # url = "https://wenku.baidu.com/view/{}.html".format(data)
        for i in range(random.randint(2, 5)):
            # driver.get(url)
            print(i)
            print(url)
            requests.get(url, headers=headers)
            time.sleep(0.1)

