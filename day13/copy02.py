# coding=utf-8
# @Time     :2020/4/23 0023 10:08
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :copy02.py
# @Software :PyCharm
import os

# 文件复制 将p4文件夹下的文件(p4下面有文件夹pp)复制到p2文件夹中
src_path = r'E:\Files_plus\Project01\QF_Python\day13_test\p4'
target_path = r'E:\Files_plus\Project01\QF_Python\day13_test\p2'


def copy(src_path, target_path):  # src_path: p4 target_path:p2
    # 获取文件夹里面内容
    filelist = os.listdir(src_path)
    print(filelist)
    #遍历列表
    for file in filelist:
        # 路径拼接
        path = os.path.join(src_path, file)
        # 判断是文件夹还是文件
        if os.path.isdir(path):
            # 递归调用copy
            copy(path, target_path)  # src_path : pp target_path:p2
        else:
            # 不是文件夹则直接进行复制
            with open(path, 'rb') as rstream:
                container = rstream.read()

                path1 = os.path.join(target_path, file)
                with open(path1, 'wb') as wstream:
                    wstream.write(container)
    else:
        print('复制完毕')


# 调用函数
copy(src_path, target_path)