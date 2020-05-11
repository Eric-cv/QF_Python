# coding=utf-8
# @Time     :2020/4/24 0024 11:23
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :exception03.py
# @Software :PyCharm
'''
try：
    有可能有异常的代码
except 类型1:
    pass
    ...
else:
    如果try中没有发生异常则进入的代码

注意：如果使用else则在try中不能出现return，因为return将结果返回，终止了else的到达

'''


def func():
    try:
        n1 = int(input('输入数字：'))
        print(n1)
        return n1
    except ValueError:
        print('必须是数字...')
        return 2
    else:
        print('数字输入完毕！')  # 没有异常才会执行的代码


func()
