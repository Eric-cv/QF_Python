# coding=utf-8
# @Time     :2020/4/30 0030 23:33
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :Loop_import2.py
# @Software :PyCharm
# from Loop_import1 import task1


def func():
    from Loop_import1 import task1
    print('------Loop_import2的func---1---')
    task1()
    print('------Loop_import2的func---2---')
