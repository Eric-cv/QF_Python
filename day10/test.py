# coding=utf-8
# @Time     :2020/4/3 0003 23:48
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :test,py.py
# @Software :PyCharm

s = {1, 2, 3, 4, 5}

for i in s:
    print(i)

for index, i in enumerate(s):
    print(index, i)

list1 = []
index = 0
for i in s:
    t1 = (index, i)
    list1.append(t1)

    index += 1

print(list1)

for index, value in list1:
    print(index, value)


# 复用

def enumerate(value):
    list1 = []
    index = 0
    for i in value:
        t1 = (index, i)
        list1.append(t1)

        index += 1

    print(list1)


s = [2, 5, 7, 9, 0, 7]
enumerate(s)