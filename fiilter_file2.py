import os
import shutil
import math

# doc_name = "zuowen"
# doc_name = "zuowen_zhouer"
# doc_name = "zuowen_zhousan"
# doc_name_ = "xuekewang_new"
# doc_name_ = "xuekewang"
#
# dir_list = os.listdir("./{}".format(doc_name_))
dir_list = os.listdir(r"E:\tmp\short_file")
print(dir_list)

list_data = []

count = 0
doc_page = 1

n = 0
for filename in dir_list:
    oldname = r"E:\tmp\short_file\{}".format(filename)
    new_file_name = filename.replace("[中学联盟]·", "")
    new_file_name = new_file_name.replace("【教学资源网·世纪金榜】", "")
    new_file_name = new_file_name.replace("【免费】", "")
    new_file_name = new_file_name.replace("【免费精品】", "")
    new_file_name = new_file_name.replace("【名校课堂】", "")
    new_file_name = new_file_name.replace("【同步备课精品课件】", "")
    new_file_name = new_file_name.replace("【同步必备】", "")
    new_file_name = new_file_name.replace("【同步教案】", "")
    new_file_name = new_file_name.replace("【zktp】", "")
    new_file_name = new_file_name.replace("【zktp】", "")
    new_file_name = new_file_name.replace("【SYB】", "")
    new_file_name = new_file_name.replace("【百分闯关】", "")
    new_file_name = new_file_name.replace("【精品预习案】", "")




    # 百度文库docx使用
    # new_file_name = filename.replace("(√)", "")
    # new_file_name = new_file_name.replace("(word完整版)", "")
    # new_file_name = new_file_name.replace("(精品)", "")
    # new_file_name = new_file_name.replace("(精华版)", "")
    # new_file_name = new_file_name.replace("(推荐下载)", "")
    # new_file_name = new_file_name.replace("(完整word)", "")
    # new_file_name = new_file_name.replace("(完整)", "")
    # new_file_name = new_file_name.replace("(完整版)", "")
    # new_file_name = new_file_name.replace("(完整word版)", "")
    # new_file_name = new_file_name.replace("PPT", "")
    # new_file_name = new_file_name.replace("(pdf)", "")
    # new_file_name = new_file_name.replace(".pdf", "")
    # new_file_name = new_file_name.replace("pdf", "")
    # new_file_name = new_file_name.replace("【精华】", "")
    # new_file_name = new_file_name.replace("【精品】", "")
    # new_file_name = new_file_name.replace("【精】", "")
    # new_file_name = new_file_name.replace("【热门】", "")
    # new_file_name = new_file_name.replace("【最新】", "")
    # new_file_name = new_file_name.replace("〖精品〗", "")
    # new_file_name = new_file_name.replace("【精选】", "")
    # new_file_name = new_file_name.replace("〖精选〗", "")
    # new_file_name = new_file_name.replace("【精选版】", "")
    # new_file_name = new_file_name.replace("(推荐文档)", "")
    # new_file_name = new_file_name.replace("【英语】", "")
    # new_file_name = new_file_name.replace("【精编】", "")
    # new_file_name = new_file_name.replace("【精品文档】", "")
    # new_file_name = new_file_name.replace("〖推荐〗", "")
    # new_file_name = new_file_name.replace("【推荐】", "")
    # new_file_name = new_file_name.replace("【独家】", "")
    # new_file_name = new_file_name.replace("修订稿", "")
    # new_file_name = new_file_name.replace("精修订", "")
    # new_file_name = new_file_name.replace("完整版", "")







    # new_file_name = new_file_name.replace("——", "")
    # new_file_name = new_file_name.replace("%", "")
    # new_file_name = new_file_name.replace("（多吉制作）", "")
    # new_file_name = new_file_name.replace("@", "")
    # # new_file_name = new_file_name.replace("_", "")
    # new_file_name = new_file_name.replace("[", "")
    # new_file_name = new_file_name.replace("]", "")
    # new_file_name = new_file_name.replace("★", "")
    # new_file_name = new_file_name.replace("【免费】", "")
    # new_file_name = new_file_name.replace("免费", "")
    # new_file_name = new_file_name.replace("下载", "")
    # new_file_name = new_file_name.replace("放送", "")
    # new_file_name = new_file_name.replace("-锐普PPT论坛", "")
    # new_file_name = new_file_name.replace("锐普PPT", "")
    # new_file_name = new_file_name.replace("（锐普PPT论坛）", "")
    # new_file_name = new_file_name.replace("锐普原创-", "")
    #

    # new_file_name = new_file_name.replace("锐普", "")
    # # new_file_name = filename.replace("《金榜学案》", "")
    # # new_file_name = new_file_name.replace("【教学资源网·世纪金榜】", "")
    # # new_file_name = new_file_name.replace(".ppt.ppt", ".ppt")
    # # new_file_name = new_file_name.replace("金榜学案", "")
    # # new_file_name = new_file_name.replace("(二)", "_2")
    # # new_file_name = new_file_name.replace("（三）", "_3")
    # # new_file_name = new_file_name.replace("(一)", "_1")
    # # new_file_name = new_file_name.replace("(三)", "_3")
    # # new_file_name = new_file_name.replace("﹡", "")
    # # new_file_name = new_file_name.replace("7下", "7年级下册")
    # # new_file_name = new_file_name.replace("7上", "7年级上册")
    # # new_file_name = new_file_name.replace("8下", "8年级下册")
    # # new_file_name = new_file_name.replace("8上", "8年级上册")
    # # new_file_name = new_file_name.replace("9下", "9年级下册")
    # # new_file_name = new_file_name.replace("9上", "9年级上册")
    # #
    # # new_file_name = new_file_name.replace("七下", "七年级下册")
    # # new_file_name = new_file_name.replace("七上", "七年级上册")
    # # new_file_name = new_file_name.replace("八下", "八年级下册")
    # # new_file_name = new_file_name.replace("八上", "八年级上册")
    # # new_file_name = new_file_name.replace("九下", "九年级下册")
    # # new_file_name = new_file_name.replace("九上", "九年级上册")
    # #
    # # new_file_name = new_file_name.replace("、", "_")
    # # new_file_name = new_file_name.replace("（一）", "_1")
    # # new_file_name = new_file_name.replace("（二）", "_2")
    # # new_file_name = new_file_name.replace("（四）", "_4")
    # # new_file_name = new_file_name.replace("（五）", "_5")
    # # new_file_name = new_file_name.replace("（六）", "_6")
    # # new_file_name = new_file_name.replace("（七）", "_7")
    # # new_file_name = new_file_name.replace("（八）", "_8")
    # # new_file_name = new_file_name.replace("（九）", "_9")
    # # new_file_name = new_file_name.replace("（十）", "_10")
    # # new_file_name = new_file_name.replace("、", "_")
    # # new_file_name = new_file_name.replace("  һ", "")
    # # new_file_name = new_file_name.replace(" ʲ ô", "")
    # # new_file_name = new_file_name.replace("ѹǿ", "")
    # # new_file_name = new_file_name.replace(" Ϣ ", "")
    # # new_file_name = new_file_name.replace("ƪ ", "")
    # # new_file_name = new_file_name.replace("֮ ", "的")
    # # new_file_name = new_file_name.replace("ͶӰ  ", "")
    # new_file_name = filename
    newname = r"E:\爬虫电脑Google-3-6\总文件\{}".format(new_file_name)
    try:
        shutil.move(oldname, newname)  # 用os模块中的rename方法对文件改名
    except:
        pass

    # # if "www" in filename or "免费" in filename:
    # if "www" in filename:
    #     try:
    #         os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
    #     except:
    #         pass


# for i in dir_list:
#     oldname = path + os.sep + fileList[n]  # os.sep添加系统分隔符
#
#     # 设置新文件名
#     newname = path + os.sep + 'a' + str(n + 1) + '.JPG'
#
#     os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
#     print(oldname, '======>', newname)

# n += 1
# for i in range(len(dir_list)):
#     i = i + 1
#     doc_name = math.floor(i / 20)
#     if not os.path.exists("./wenzhang/{}".format(doc_name)):
#         os.makedirs("./wenzhang/{}".format(doc_name))
#     shutil.copyfile("./{}/{}".format(doc_name_, dir_list[i - 1]), "./wenzhang/{}/{}".format(doc_name, dir_list[i - 1]))

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
