# coding=utf-8
# @Time     :2020/4/25 0025 9:25
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :list01.py
# @Software :PyCharm
# 列表推导式 集合推导式 字典推导式
# 旧的列表 ----> 新的列表

# 1. 列表推导式：格式：[表达式 for 变量 in 旧列表]
# 或者 [表达式 for 变量 in 旧列表 if 条件]

# 过滤掉长度小于等于3的人名
names = ['tom', 'lily', 'abc', 'jack', 'steven', 'hob', 'ha']

result = [name for name in names if len(name) > 3]
print(result)

# 追加每个元素首字母大写的要求
result = [name.capitalize() for name in names if len(name) > 3]
print(result)

# 将1-100之间能被3整除，组成一个新的列表
newlist = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(newlist)

'''
def func(names):
    newlist = []
    for name in names:
        if len(name)>3:
        newlist.append(name)
    return newlist
'''


# 构成0-5的偶数 0-10的奇数构成的列表
# [(0, 1), (0, 3)...,(0, 9),...(4, 1), (4, 3),...,(4, 9) ]
# 常规函数方法

def func():
    list = []
    for i in range(5):  # 偶数
        if i % 2 == 0:
            for j in range(10):
                if j % 2 != 0:
                    list.append((i, j))
    return list


x = func()
print(x)

# 列表推导式1行搞定
list1 = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(list1)

# list1 = [[1,2,3], [4,5,6], [7,8,9], [1,3,5]]  -----> newlist = [3,6,9,5]

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]
newlist = [list[-1] for list in list1]
print(newlist)

dict1 = {'name': 'tom', 'salary': 5000}
dict2 = {'name': 'lucy', 'salary': 8000}
dict3 = {'name': 'jack', 'salary': 4500}
dict4 = {'name': 'lily', 'salary': 3000}
list1 = [dict1, dict2, dict3, dict4]  # [{}, {}, {}]
# if else 列表推导式
# if 薪资大于5000加200， 低于5000加500
# 格式：[条件成立执行 if 条件 else 条件不成立执行 for 变量 in 旧列表]
newlist = [employee['salary'] + 200 if employee['salary'] > 5000 else employee['salary'] + 500 for employee in list1]
print(newlist)  # [5500, 8200, 5000, 3500]

# 集合推导式 {}  类似于列表推导式的基础上添加了一个去除重复项的功能
list1 = [1, 2, 1, 3, 5, 2, 1]
set1 = {x - 1 for x in list1 if x > 5}
print(set1)

# 字典推导式
dict1 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'C'}

newdict = {value: key for key, value in dict1.items()}
print(newdict)
