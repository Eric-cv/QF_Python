# coding=utf-8
# @Time     :2020/4/23 0023 9:46
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :copy.py
# @Software :PyCharm
import os
# 文件复制 将p4文件夹下的文件(p4下面没有文件夹)复制到p1文件夹中
src_path = r'E:\Files_plus\Project01\QF_Python\day13_test\p4'
target_path = r'E:\Files_plus\Project01\QF_Python\day13_test\p2'

# 封装成函数
def copy(src, target):
    if os.path.isdir(src) and os.path.isdir(target):
        filelist = os.listdir(src)

        for file in filelist:
            path = os.path.join(src, file)
            with open(path, 'rb') as rstream:
                container = rstream.read()

                path1 = os.path.join(target, file)
                with open(path1, 'wb') as wstream:
                    wstream.write(container)
        else:
            print('复制完毕')

# 调用函数
copy(src_path, target_path)
