import requests
from lxml import etree
import json

# 构建url
# 构建url
# url = 'http://tiku.gaokao.com/detail/28715'
# url = 'http://cz.jb1000.com/Details/DownLoad.aspx?infoid={}'
url = 'http://jb1000.com/Details/DownLoad.aspx?infoid={}'
# url = 'http://tiku.gaokao.com/gaozhong/a259?pg=10'

headers = {
    # 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


def write_json_file(file_path, load_dict):
    with open(file_path, "w") as dump_f:
        json.dump(load_dict, dump_f)


list_data = []
# for i in range(728521):
start_num = 800797
end_num = 900001
# for i in range(600000, start_num):
for i in range(start_num, end_num):
    # for i in range(20):
    try:
        resp = requests.get(url.format(i), headers=headers)
        html = etree.HTML(resp.content.decode(encoding="gbk"))
        # html_all = resp.content.decode(encoding="gbk")
        # print(html)
        # html = etree.HTML(html_all)
        # print(html)

        content_list = html.xpath('//*[@id="pnlother"]/div[1]/div[2]/span[1]/@data-value')
        # content_list = html.xpath('/html/body/div[6]/div[1]/div[1]/h1')
        # print(content_list[0])

        if content_list[0] == "0":
            print("可以下载，序号：{}".format(i))
            list_data.append([i, None])
        else:
            print("无法下载，序号：{}，金币：{}".format(i, content_list[0]))
            continue
    except:
        print("出现异常，序号：{}".format(i))

    if i % 20 == 0:
        print("存储20的倍数")
        dict_data = {"down_list": list_data}
        write_json_file("./jiaoxue_{}.json".format(str(end_num)), dict_data)

dict_data = {"down_list": list_data}
write_json_file("./jiaoxue_{}.json".format(str(end_num)), dict_data)
