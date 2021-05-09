import os
import shutil
import math

# doc_name = "zuowen"
# doc_name = "zuowen_zhouer"
# doc_name = "zuowen_zhousan"
# doc_name_ = "xuekewang_new"
doc_name_ = "xuekewang"

dir_list1 = os.listdir("E:\ppt_dowm\总文件")
dir_list2 = os.listdir("E:\金锄头上传\pass")
# print(dir_list1)
# print(dir_list2)


list_data = []
for str_data in dir_list2:
    cut_data = str_data.split(".")[0]
    list_data.append(cut_data)
    # print(str_data.split(".")[0])

print(list_data)
print(len(dir_list2))
print(len(list_data))

# list_data = []
#
# count = 0
# doc_page = 1
#
# n = 0
for filename in dir_list1:
    cut_str = filename.split(".")[0]

    # filename_x = filename + "x"
    if cut_str in list_data:
        print(filename)
        shutil.move("E:\ppt_dowm\总文件\{}".format(filename), r"E:\ppt_dowm\重复\{}".format(filename))
        # shutil.move("./xuekewang/{}".format(filename_x), "./xuekewang1/{}".format(filename_x))
        # print(filename_x)

