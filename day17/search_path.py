# coding=utf-8
# @Time     :2020/5/1 0001 0:07
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :search_path.py
# @Software :PyCharm
'''
当你导入一个模块时，python解释器对模块位置的搜索顺序是：
1.当前目录
2.如果不存在当前目录，python则搜索在shell变量PYTHONPATH下的每一个目录
3.如果都找不到，python会查看默认路径，UNIX下，默认路径一般为/usr/local/bin/python/
模块的搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由当前安装过程决定的默认目录。
'''

'''
自定义模块
系统模块
  sys模块
'''
# from article
import sys

print(sys.path)  # 系统默认对包和模块的搜索路径
print(sys.version)  # python解释器版本
print(sys.argv)  # 运行程序时的一些参数，argv是一个列表
