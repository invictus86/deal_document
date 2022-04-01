import os
import math

list_dir_current = os.listdir("curent_txt")
# list_dir_used = os.listdir("used_txt")
list_dir_used = []

all_url_current = []
for file_name in list_dir_current:
    print(file_name + " curent_txt")
    with open("./curent_txt/{}".format(file_name), "r") as f:
        all_file_url = f.readlines()
    all_url_current = all_url_current + all_file_url
    all_url_current = list(set(all_url_current))
print(len(all_url_current))
all_url_used = []
for file_name in list_dir_used:
    print(file_name + " used_txt")
    with open("./used_txt/{}".format(file_name), "r") as f:
        all_file_url_used = f.readlines()
    all_url_used = all_url_used + all_file_url_used
    all_url_used = list(set(all_url_used))
print(len(all_url_used))
finally_url = list(set(all_url_current) - set(all_url_used))


# finally_url = []
# for url in all_url_current:
#     print(url)
#     if url in all_url_used:
#         pass
#     else:
#         finally_url.append(url)

print(len(finally_url))
# file_num = math.ceil(len(finally_url) / 2000)
file_num = math.ceil(len(finally_url) / 2000)
print(file_num)

import datetime
#获取时间函数，把当前时间格式化为str类型nowdate.strftime('%Y-%m-%d %H:%M:%S')
def getLastDate():
    return datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

code = getLastDate()
print(code)

for i in range(file_num):
    print(i)
    path = "out_put_txt/{}-{}".format(code, i)
    isExists = os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.makedirs(path)
        print(path + ' 目录创建成功')
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
    with open("out_put_txt/{}-{}/{}-{}.txt".format(code, i, code, i), "w") as f:
        if i == (file_num - 1):
            for url in finally_url[(2000 * i):len(finally_url)]:
                f.write(url)
        else:
            for url in finally_url[(0 + i * 2000):(2000 * (i + 1))]:
                f.write(url)

