# coding=utf-8
# @Time     :2020/4/24 0024 11:30
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :exception04.py
# @Software :PyCharm
# 异常情况4
'''
# 文件操作 stream = open(...)  stream.read() stream.close()
# 数据库操作： close()
try:
    pass
except:
    pass
finally:
    pass

finally是一定会进入的模块，不管有没有异常出现，常用于关闭文件
'''


def func():
    stream = None
    try:
        stream = open(r'E:\Files_plus\Project01\QF_Python\day13\01.txt', 'r')
        container = stream.read()
        print(container)
        return 1
    except Exception as err:
        print(err)
        return 2
    finally:
        print('----finally----')
        if stream:
            stream.close()
        return 3


x = func()
print(x)

# 注意：当finally模块和return同时出现时，一定会进入finally，但return有几种情况，以上面为例：
# try中return 1, except中return 2, finally中return 3
# 有以下几种情况：
# 1) 如果finally中有return 3，则不论前面进入的是try还是except，最后finally的返回值都会覆盖前面的返回值，返回3
# 2) 如果finally中没有return，则如果进入try，则返回1，如果进入except，则返回2