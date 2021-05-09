import os
import shutil
import math

# doc_name = "zuowen"
# doc_name = "zuowen_zhouer"
# doc_name = "zuowen_zhousan"
# doc_name_ = "xuekewang_new"
doc_name_ = "xuekewang"

dir_list = os.listdir("./{}".format(doc_name_))
print(dir_list)

list_data = []

count = 0
doc_page = 1

n = 0
for filename in dir_list:

    filename_x = filename + "x"
    if filename_x in dir_list:
        shutil.move("./xuekewang/{}".format(filename), "./xuekewang1/{}".format(filename))
        shutil.move("./xuekewang/{}".format(filename_x), "./xuekewang1/{}".format(filename_x))
        print(filename_x)

