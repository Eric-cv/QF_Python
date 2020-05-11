# coding=utf-8
# @Time     :2020/4/22 0022 0:14
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :file01.py
# @Software :PyCharm
# 文件操作
'''
文件上传
保存log

系统函数：
open(file, mode, buffering )

读：
open(path/filename, 'rt') ----->返回值:stream  (管道)
container = stream.read() -----> 读取管道中的内容
注意：如果传递的path/filename有误， 则会报错：FileNotFoundError
如果是图片则不能使用默认是读取方式:mode = 'rb'

总结：
read()  读取所有内容
readline() 每次读取一行内容
readlines() 读取所有行保存到列表中
readable() 判断是否可读的
'''

stream = open(r'..\day11\aaa.txt')
# container = stream.read()
# print(container)

# stream = open(r'..\day11\a1.docx')
# container = stream.read()
# print(container)


result = stream.readable()  # 判断是否可以读取 :True False
print(result)

# while True:
#     line = stream.readline()   # 一次读一行
#     print(line)
#     if not line:
#         break


lines = stream.readlines()
print(lines)

for i in lines:
    print(i)


stream = open(r'../day11/lena.jpg', 'rb')
container = stream.read()
print(container)