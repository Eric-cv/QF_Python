# coding=utf-8
# @Time     :2020/4/22 0022 10:45
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :os01.py
# @Software :PyCharm

# 模块：os.py
'''
os.path
os.path.dirname(__file__)  # 获取当前文件所在目录
os.path.join(path,'')  # 返回拼接后的一个新路径
'''
import os

# print(os.path)
# path = os.path.dirname(__file__) # 获取当前文件所在的文件目录（绝对路径）
# print(path)
# print(type(path))
# # 在文件夹下拼接文件的名字
# result = os.path.join(path, 'leno.jpg')
# print(result)

# ..\day11\leno.jpg  ----> 保存在当前文件的所在目录
with open(r'..\day11\a1.jpg', 'rb') as stream:
    # 读图片的方式创建流到指定路径
    container = stream.read()  # 读取文件内容到缓存
    print(stream.name)
    file = stream.name
    print(file.rfind('\\'))
    filename = file[file.rfind('\\')+1 :]  # 截取文件名
    print(filename)

    path = os.path.dirname(__file__)
    path1 = os.path.join(path, filename) # 得到当前路径下同名文件
    with open(path1, 'wb') as wstream:
        # 写图片的形式创建流到指定路径
        wstream.write(container) # 把缓存内容写到图片中

print('文件复制完成！')