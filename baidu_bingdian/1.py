# -*- coding:utf-8 -*-
import datetime
#获取时间函数，把当前时间格式化为str类型nowdate.strftime('%Y-%m-%d %H:%M:%S')
def getLastDate():
    return datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

code = getLastDate()
print(code)