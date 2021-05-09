from os import startfile
from os.path import splitext
from docx import Document
import os


def deal_word_file(fn, fn_new):
    fn = fn
    fn_new = fn_new
    # fn_new = "_new".join(splitext(fn))

    word = Document(fn)
    # 取消奇数偶数页
    word.settings.odd_and_even_pages_header_footer = False

    for section in word.sections:
        # 取消首页不同
        section.different_first_page_header_footer = False
        # 删除页眉页脚
        section.header.is_linked_to_previous = True
        section.footer.is_linked_to_previous = True

    word.save(fn_new)
    # startfile(fn_new)


doc_name = "xuekewang"
doc_name1 = "xuekewang1"

dir_list = os.listdir("./{}".format(doc_name))
# print(dir_list)

# for file_name in dir_list:
#     try:
#         deal_word_file("./{}/{}".format(doc_name, file_name), "./{}/{}".format(doc_name1, file_name))
#         print("处理文档成功：{}， {}".format(file_name, dir_list.index(file_name)))
#     except:
#         print("处理文档失败：{}， {}".format(file_name, dir_list.index(file_name)))


from win32com import client as wc #导入模块


def doc_to_docx(file):
    word = wc.Dispatch("Word.Application") # 打开word应用程序
    doc = word.Documents.Open(file) #打开word文件
    doc.SaveAs("{}x".format(file), 12)#另存为后缀为".docx"的文件，其中参数12指docx文件
    doc.Close() #关闭原来word文件
    word.Quit()
    print("完成！")
    return "{}x".format(file)


if __name__ == '__main__':

    for file_name in dir_list:
        if file_name[-4:] == "docx":
            print("跳过：{}，{}".format(file_name, dir_list.index(file_name)))
            # print(file_name)
            # print(dir_list.index(file_name))
            continue
        # deal_word_file("./{}/{}".format(doc_name, file_name), "./{}/{}".format(doc_name1, file_name))
    # file = r"F:\code\get_baiduwenku\222.doc"
        try:
            doc_to_docx(r"F:\code\get_baiduwenku\xuekewang\{}".format(file_name))
            print(file_name)
            print(dir_list.index(file_name))
        except:
            print("出异常了：{} ，{}".format(file_name, dir_list.index(file_name)))
            continue
