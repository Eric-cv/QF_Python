# coding=utf-8
# @Time     :2020/4/22 0022 10:30
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :file03.py
# @Software :PyCharm

# 文件的复制
'''
源文件：path1 = '..\day11\lena.jpg'
目标文件 path2 = 'lena.jpg'
with 结合open使用，可以帮助我们自动释放资源
'''
# copy单个文件
with open(r'..\day11\lena.jpg', 'rb') as stream:
    # 读图片的方式创建流到指定路径
    container = stream.read()  # 读取文件内容到缓存

    with open(r'lena.jpg', 'wb') as wstream:
        # 写图片的形式创建流到指定路径
        wstream.write(container) # 把缓存内容写到图片中

print('文件复制完成！')


