# coding=utf-8
# @Time     :2020/4/11 0011 23:55
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func02.py
# @Software :PyCharm

a = 100  # 全局变量
print(globals())

def func():
    # 声明变量
    b = 99

    # 声明函数
    def inner_func():
        global a
        nonlocal b
        c = 88
        # 尝试修改
        c += 12
        b += 1
        a += 10
        # 尝试打印
        print(a, b, c)

    # 调用内部函数
    inner_func()
    # 使用locals()内置函数进行查看，可以看到在当前函数中声明的内容有哪些
    # locals()是一个字典。key:value
    # {'inner_func': <function func.<locals>.inner_func at 0x000001DBC1E62730>, 'b': 100}
    print(locals())


# 调用函数
func()
