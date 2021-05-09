import requests
import zipfile
import os


def download_ppt(down_url, image_url):
    resp = requests.get(down_url)
    file_name = down_url[38:]
    print(file_name)
    doc_path = file_name[:-4]
    print(doc_path)
    isExists = os.path.exists("./ppt_doc/{}".format(doc_path))

    # 判断结果
    if not isExists:
        os.makedirs("./ppt_doc/{}".format(doc_path))

        print(doc_path + ' 创建成功')
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(doc_path + ' 目录已存在')

    with open("./ppt_doc/{}/{}".format(doc_path, file_name), "wb") as f:
        f.write(resp.content)

    image_resp = requests.get(image_url)
    image_name = image_url[40:]
    print(image_name)
    with open("./ppt_doc/{}/{}".format(doc_path, image_name), "wb") as f:
        f.write(image_resp.content)

    '''
    基本格式：zipfile.ZipFile(filename[,mode[,compression[,allowZip64]]])
    mode：可选 r,w,a 代表不同的打开文件的方式；r 只读；w 重写；a 添加
    compression：指出这个 zipfile 用什么压缩方法，默认是 ZIP_STORED，另一种选择是 ZIP_DEFLATED；
    allowZip64：bool型变量，当设置为True时可以创建大于 2G 的 zip 文件，默认值 True；
    
    '''
    # zip_file = zipfile.ZipFile("./ppt_doc/{}/{}".format(doc_path, file_name))
    # zip_list = zip_file.namelist()  # 得到压缩包里所有文件
    #
    # for f in zip_list:
    #     zip_file.extract(f, "./ppt_doc/{}".format(doc_path))  # 循环解压文件到指定目录
    #
    # zip_file.close()  # 关闭文件，必须有，释放内存
    #
    # # print(resp.content)


if __name__ == '__main__':
    download_ppt("http://ppt.1ppt.com/uploads/soft/2012/1-201221220505.zip", 'http://img.1ppt.com/uploads/allimg/2101/1-2101220911260-L.jpg')
