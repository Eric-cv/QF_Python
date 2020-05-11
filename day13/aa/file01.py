# coding=utf-8
# @Time     :2020/4/22 0022 22:57
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :file01.py
# @Software :PyCharm
import os

# 判断是否为绝对路径
# os.path.isabs()

# 使用绝对路径
r = os.path.isabs(r'E:\Files_plus\Project01\QF_Python\day12\a1.jpg')
print(r)

# 使用相对路径
r1 = os.path.isabs(r'..\day12\a1.jpg')  # ..\ 表示返回当前文件的上一级
print(r1)

# 获取当前文件夹的路径 path of directory name
path1 = os.path.dirname(__file__)
print(path1)

# 获取当前文件夹的路径
path2 = os.getcwd()  # 类似os.path.dirname(__file__)
print(path2)

# 获取当前文件的路径
path3 = os.path.abspath(__file__)  # __file__表示当前文件
print(path3)

# 获取xx文件的路径
path4 = os.path.abspath('aa.txt')
print(path4)

# os.path.split(path)
path = r'E:\Files_plus\Project01\QF_Python\day13\aa\file01.py'
# 获取文件名
result = os.path.split(path)  # 分割文件与文件名
print(result)  # ('E:\\Files_plus\\Project01\\QF_Python', 'day13\x07a\x0cile01.py')
print('文件名为：', result[1])

filename1 = path[path.rfind('\\') + 1:]
print('文件名为：', filename1)

result = os.path.splitext(path)  # 分割文件与扩展名
print(result)  # ('E:\\Files_plus\\Project01\\QF_Python\\day13\\aa\\file01', '.py')
print('文件扩展名：', result[1])

# os.path.getsize() 获取文件大小，单位是字节
size = os.path.getsize(path)
print(size)

# os.path.join 路径拼接
result = os.path.join(os.getcwd(), 'file01.py')
print(result)  # E:\Files_plus\Project01\QF_Python\day13\aa\file01.py

'''
os.path.dirname(__file__)
os.getcwd()
os.path.abspath()
os.path.join()
os.path.split()
os.path.splitext()
os.path.getsize()

os.path.isabs() # 是绝对路径吗？
os.path.isfile() # 是文件吗？
os.path.isdir() # 是文件夹吗？
'''
