# coding=utf-8
# @Time     :2020/4/2 0002 0:36
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func.01.py.py
# @Software :PyCharm

# 定义函数：完成随机数的产生
# 自动格式化： Alt+ctrl+f
import random


def generate_random():
    for i in range(10):
        ran = random.randint(1, 20)
        print(ran)


print(generate_random)  # 打印函数名，函数名是一个地址，储存函数体的地址
# <function generate_random at 0x00000205707426A8>
# 调用：函数名()  找到函数并执行函数体的内容
print('-----------')
generate_random()
print('-----------')
generate_random()
