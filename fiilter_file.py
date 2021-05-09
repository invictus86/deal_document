import os
import shutil

# doc_name = "zuowen"
# doc_name = "zuowen_zhouer"
# doc_name = "zuowen_zhousan"
doc_name = "zuowen_gaokao"

dir_list = os.listdir("./{}".format(doc_name))
# print(dir_list)

list_data = []

for file_name in dir_list:
    cut_file_name = file_name[:-4]
    # print(cut_file_name)
    cut_file_name_daan = cut_file_name + "答案"
    doc_cut_file = cut_file_name_daan + ".doc"
    if doc_cut_file in dir_list:
        list_data.append(file_name)
        list_data.append(doc_cut_file)

print(len(list_data))

for data in list_data:
    shutil.copyfile("./{}/{}".format(doc_name, data), "./doc_zuowen/{}".format(data))
    print(data)
