# coding=utf-8
# @Time     :2020/4/3 0003 10:07
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func02.py
# @Software :PyCharm

#  函数：带参数的
'''
def 函数名(参数,参数...):
    函数体
调用：
    pass
'''

# alt + enter 快速提示
#  求随机数的函数，产生的个数？？？
import random


def generate_random(number):  # 形参：形式上的参数  number=5
    for i in range(number):
        ran = random.randint(1, 20)
        print(ran)


print(generate_random)

# 调用
generate_random(5)  # 实参：实际的参数 具体的值
generate_random(8)


# 求加法的函数
def add(a, b):
    result = a + b
    print('和', result)


# 调用
add(2, 3)
add(1, 1)
