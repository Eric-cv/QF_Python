# coding=utf-8
# @Time     :2020/4/30 0030 23:30
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :Loop_import1.py
# @Software :PyCharm
'''
    循环导入：大型的python项目中，需要很多的py文件，由于架构不当，可能会出现模块之间的相互导入
    A:模块
        def test():
            f()
    B:模块
        def f():
            test()

    避免产生循环导入：
    1.重新架构
    2.将导入的语句放在函数里面
    3.把导入语句放在模块的最后
'''
from Loop_import2 import func


def task1():
    print('------task1------')


def task2():
    print('------task2-------')
    func()

# 调用task1
if __name__ == '__main__':
    task1()  # ------task1------
    task2()  # ------task2-------
             # ------Loop_import2的func---1---
             # ------task1------
             # ------Loop_import2的func---2------