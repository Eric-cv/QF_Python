# coding=utf-8
# @Time     :2020/4/11 0011 23:13
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func01.py
# @Software :PyCharm

# 内部函数
'''
特点：
1.可以访问外部函数的变量
2.内部函数可以修改外部函数的可变类型的变量，如list1
3.内部函数修改全局的不可变变量时，需要在内部函数声明global 变量名
  内部函数修改外部函数的不可变变量时，需要在内部函数声明nonlocal 变量名
4.locals()查看本地变量有哪些，以字典的形式输出
  globals()查看全局变量有哪些，以字典的形式输出，里面会有一些系统的键值对
'''
def func():
    # 声明变量
    n = 100  # 局部变量
    list1 = [3, 6, 9, 4]   # 局部变量

    # 声明内部函数
    def inner_func():
        nonlocal n
        # 对list1里面的元素进行加n操作
        # 0 --> 3
        for index, i in enumerate(list1):
            list1[index] = i + n

        list1.sort()

        # 修改n变量
        n += 101

    # 调用一下内部函数
    inner_func()
    print('打印老大n', n)
    print('打印老二list1', list1)

# 调用 func
func()