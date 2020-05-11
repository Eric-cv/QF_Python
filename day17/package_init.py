# coding=utf-8
# @Time     :2020/4/30 0030 22:38
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :package_init.py
# @Software :PyCharm
'''
__init__.py 文件
当导入包的时候，默认调用包中的__init__.py文件
作用：
1.当导入包的时候，把一些初始化的函数，变量，类定义在__init__.py文件中
2.此文件中函数，变量等的访问，只需要通过包名.函数...
3.结合__all__=[通过*可以访问的模块]
'''
# 直接导入包user
import user  # user的__init__文件
# 从包user中导入models模块的User类
from user.models import User  # user的__init__文件
user.create_app()
user.printA()

# from 模块 import *   # 表示可以使用模块里面的所有内容，如果没有加__all__=['', '']，
                      # 但是如果加上__all__， 只有__all__ = [’‘, ’‘]列表中的可以访问
# from 包   import *   # 表示该包中的内容（模块）是不能完全访问的，就需要在__init__.py文件中
                       # 定义__all__=[可以通过*访问的模块]

from user import *

user1 = models.User('admin', '123456')
user1.show()

print(tst.MAX)