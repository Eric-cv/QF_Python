# coding=utf-8
# @Time     :2020/5/1 0001 14:13
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :datetime02.py
# @Software :PyCharm

# datetime：time模块的升级版
'''
datetime模块：
    time 时间
    date 日期    （data  数据）
    datetime   日期时间  now
    timedelta   时间差   timedelta(day='', weeks='', ...)
'''

import datetime
import time

print(datetime.time.hour)  # 对象 <attribute 'hour' of 'datetime.time' objects>
# print(time.localtime().tm_hour)

# 因为date是类，所有要求创建对象
d = datetime.date(2019, 6, 20)
print(d.day)  # 20
print(datetime.date.ctime(d))  # Thu Jun 20 00:00:00 2019

# datetime, timedelta
print(datetime.date.today())  # 2020-05-01
timedel = datetime.timedelta(hours=2)  # 时间差2小时
print(timedel)  # 2:00:00
timedel = datetime.timedelta(weeks=3)  # 时间差3周
print(timedel)  # 21 days, 0:00:00

# datetime.datetime.now() -----> 得到当前的日期和时间
now = datetime.datetime.now()
print(now)  # 2020-05-01 14:40:28.225287
result = now + timedel
print(result)  # 2020-05-22 14:40:28.225287

# 缓存：数据库redis 作为缓存  redis.set(key, value, 时间差) 会话：session
