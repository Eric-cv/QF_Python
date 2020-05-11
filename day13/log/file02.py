# coding=utf-8
# @Time     :2020/4/22 0022 22:57
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :file01.py
# @Software :PyCharm

# os path 里面的函数
# os 中函数
import os

dir = os.getcwd()  # 获取当前文件夹的路径
print(dir)
# 返回指定目录下的所有文件与文件夹
all = os.listdir(r'E:\Files_plus\Project01\QF_Python\day13')
print(all)

path = r'/QF_Python/day13_test'
# 创建文件夹
# f = os.mkdir(path)
# print(f)  # None 无返回值

# 判断文件是否存在
if not os.path.exists(path):
    f = os.mkdir(path)
    print(f)  # None 无返回值

# # 删除文件夹
# f = os.rmdir(path)
# # OSError: [WinError 145] 目录不是空的，只能删除空文件夹
# print(f)  # None 无返回值


# path = r'E:\Files_plus\Project01\QF_Python\p2\p3\p4\aa.txt'
# # 删除文件aa.txt
# os.remove(path)

# 删除p4文件夹
# path = r'E:\Files_plus\Project01\QF_Python\p2\p3\p4'
# filelist = os.listdir(path)
# for file in filelist:
#     path1 = os.join(path, file)
#     os.remove(path1)
# else:
#     os.rmdir(path)
# print('删除成功！')
#
# # 切换目录 change directory
# path = os.getcwd()
# print(path)
# f = os.chdir(r'E:\Files_plus\Project01\QF_Python\p2')
# print(f)
# path1 = os.getcwd()
# print(path1)

path = r'/QF_Python/day13_test/p4'
r = os.listdir()
print(r)
'''
os模块下的方法：
os.getcwd() # 获取当前目录,不能传参数
os.listdir() # 浏览文件夹,可传path
os.mkdir() # 创建文件夹,可传path
os.rmdir() # 删除空文件夹,可传path
os.remove() # 删除文件,可传path
os.chdir() # 切换目录,可传path
'''
