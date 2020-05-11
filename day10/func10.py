# coding=utf-8
# @Time     :2020/4/9 0009 23:47
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func10.py
# @Software :PyCharm

#  global  变量的范围
# 局部变量  全局变量
# 声明在函数外层的是全局的，所有函数都可以访问
name = '月月'


def func():
    # 函数内部声明的变量是局部变量，局部变量仅限于在函数内部使用
    s = 'abcd'
    s += 'X'

    print(s, name)


# print(s)  报错


def func1():
    global name  # 不修改全局变量，只是获取打印，但是如果要发生修改全局变量，则需要在函数内部声明：global 变量
    print(name)  # 报错：函数内部的变量可以随便修改，但是全局变量不能在函数体中修改
    name += '会弹吉他'
    print('func1修改后的name是：', name)

def func2():
    name = '小月月'  # 局部变量与全局变量同名
    name += '弹吉他的小美女'
    print(name)


#func1()
func2()
func()
func()