import os
import shutil
import math

# doc_name = "zuowen"
# doc_name = "zuowen_zhouer"
# doc_name = "zuowen_zhousan"
doc_name_ = r"I:\新建文件夹\总文件---"

dir_list = os.listdir("{}".format(doc_name_))
print(dir_list)

list_data = []

count = 0
doc_page = 1

for i in range(len(dir_list)):
    i = i + 1
    # doc_name = math.floor(i / 20)
    doc_name = math.floor(i / 20000000)
    if not os.path.exists(r"E:\百度文库word\{}".format(doc_name)):
        os.makedirs(r"E:\百度文库word\{}".format(doc_name))
    # os.rename("{}\{}".format(doc_name_, dir_list[i - 1]), r"G:\新建文件夹_2\{}\{}".format(doc_name, dir_list[i - 1]))
    shutil.move("{}\{}".format(doc_name_, dir_list[i - 1]), r"E:\百度文库word\{}\{}".format(doc_name, dir_list[i - 1]))
    # shutil.copyfile("{}\{}".format(doc_name_, dir_list[i - 1]), r"E:\新建文件夹\{}\{}".format(doc_name, dir_list[i - 1]))


# for file_name in dir_list:
#     count = count + 1
#
#     cut_file_name = file_name[:-4]
#     # print(cut_file_name)
#     cut_file_name_daan = cut_file_name + "答案"
#     doc_cut_file = cut_file_name_daan + ".doc"
#     if doc_cut_file in dir_list:
#         list_data.append(file_name)
#         list_data.append(doc_cut_file)
#
# print(len(list_data))
#
# for data in list_data:
#     shutil.copyfile("./{}/{}".format(doc_name, data), "./doc_zuowen/{}".format(data))
#     print(data)
