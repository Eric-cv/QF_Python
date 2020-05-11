# coding=utf-8
# @Time     :2020/4/20 0020 0:21
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :Recursive_func.py
# @Software :PyCharm

# 递归函数：函数自己调用自己
'''
普通：def func():pass
匿名函数：lambda 参数： 返回结果
递归函数：普通函数的一种表现形式

特点：
1.递归函数必须设定终点（出口）
2.通常都会有一个入口
3.要知道入口是什么，出口是什么，然后自己调自己
'''


def sum(n):  # 1-n
    '''
    求和的函数
    :param n:从1到n累加求和
    :return: 求和的值
    '''
    if n == 0: # 终止条件（出口）
        return 0
    else:
        return n + sum(n - 1)


result = sum(10)  # n = 10 入口
print(result)

s = 0
for i in range(11):
    s += i
print(s)


def f1(n):
    if n>0:
        print('----->',n)
        f1(n-1)
    else:
        print('----->', n)


f1(5)