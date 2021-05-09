import requests
from lxml import etree
import os

# 需求：爬取百度贴吧的图片，保存到本地

# 流程：
# 使用循环
# 构建url、请求头
# 发送请求，获取响应
# 解析数据，使用xpath，根据贴吧列表数据，提取详情页面的title和url
# 遍历详情页，获取详情页的图片url
# 根据图片的url，发送请求，获取图片的响应数据,下载图片，wb


url = 'http://tiku.gaokao.com/gaokao/?pg={}'.format("10")
# 更换不支持js的请求头，可以获取源码中的数据
headers = {
    # 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

resp = requests.get(url, headers=headers)
# html = resp.content.decode()
html = etree.HTML(resp.content.decode())
# html = resp.content

# page_list = html.xpath('/html/body/section[2]/div[2]/div/div[2]/a')
page_list = html.xpath('/html/body/section[2]/div[1]/div/div[2]/a')
max_page = page_list[-2].text
print(max_page)

list_data = []
for i in range(int(max_page)):
    # url = 'http://tiku.gaokao.com/gaozhong/a261?pg={}'.format(str(i + 1) + "0")
    url = 'http://tiku.gaokao.com/gaokao/?pg={}'.format(str(i + 1) + "0")
    resp = requests.get(url, headers=headers)
    # html = resp.content.decode()
    html = etree.HTML(resp.content.decode())

    # href_list = html.xpath('/html/body/section[2]/div[2]/div/article/p[2]/span/a[2]/@href')
    href_list = html.xpath('/html/body/section[2]/div[1]/div/article/p[2]/span/a[2]/@href')
    # node_list = html.xpath('/html/body/section[2]/div[2]/div/article/h2/a')
    node_list = html.xpath('/html/body/section[2]/div[1]/div/article/h2/a')

    for j in range(len(node_list)):
        href = href_list[j]
        name = node_list[j].text
        print(href)
        print(name)
        list_data.append([href, name])

        # 使用requests库发送网络请求
        response = requests.get(href)
        # 打印访问百度返回的状态码
        # print(response.status_code)

        # print()
        # with open("./zuowen_zhousan/{}.doc".format(name), "wb") as f:
        with open("./zuowen_gaokao/{}.doc".format(name), "wb") as f:
            f.write(response.content)
        print(i, j)
#
print(list_data)
print(len(list_data))
