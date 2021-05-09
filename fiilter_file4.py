import os
import shutil
import math

# doc_name = "zuowen"
# doc_name = "zuowen_zhouer"
# doc_name = "zuowen_zhousan"
# doc_name = "xuekewang"
doc_name = "E:\google_download"

# dir_list = os.listdir("./{}".format(doc_name))
dir_list = os.listdir("{}".format(doc_name))
print(dir_list)

list_data = []

count = 0
doc_page = 1

for file_name in dir_list:
    # print(file_name[-7:])
    print(dir_list.index(file_name))
    #
    if "06" in file_name or "07" in file_name or "08" in file_name or "09" in file_name or "10" in file_name or "11" in file_name or "12" in file_name or "13" in file_name or "14" in file_name or "15" in file_name or "16" in file_name or "17" in file_name:
        # if file_name[-7:] == "(1).rar" or file_name[-7:] == "(1).zip" or \
        #         file_name[-7:] == "(2).rar" or file_name[-7:] == "(2).zip" or \
        #         file_name[-7:] == "(3).rar" or file_name[-7:] == "(3).zip":
        # shutil.move("./xuekewang/{}".format(file_name), "./xuekewang1/{}".format(file_name))
        shutil.move("E:\google_download\{}".format(file_name), r"E:\tmp\short_file\{}".format(file_name))


