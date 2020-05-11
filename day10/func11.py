# coding=utf-8
# @Time     :2020/4/10 0010 0:27
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func11.py
# @Software :PyCharm

# 局部和全局
# 全局变量如果是不可变在函数中进行修改需要添加global关键字
# 如果全局变量是可变的，在函数中修改的时候就不需要添加global
name = '月月'

list1 = [1, 2, 4, 6]


def func():
    name = '蕊蕊'
    print(name)
    print(list1)


def func1():
    global name
    print(name)
    name += '真漂亮!'

    # 修改列表
    list1.append(8)
    print(list1)


def func2():
    global name
    name1 = 'lucy'
    name1 += 'hhhh'
    print(name)  # 自己的
    print(name)  # 全局的

func1()
func()
