# coding=utf-8
# @Time     :2020/4/30 0030 21:47
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :tst.py
# @Software :PyCharm


'''
day17
  |-calculate.py
  |-article.py
        |-models.py
            |-Article
        |-__init__.py
        |...
  |-user.py
        |-models.py
            |-User
        |-__init__.py
        |-tst.py
'''

# 用户发表文章
# 创建用户对象
# 发表文章：文章对象

# 从tst导入user.models 的User类，article.models 的Article类
from user.models import User
from article.models import Article
# from .models import User  # 当前目录下的models里面的User类 . 表示当前目录

user = User('admin', '123456')  # ---> user是通过导入User类创建的
article = Article('个人总结', '家伟')
user.publish_article(article)

list1 = [1, 2, 5, 6, 7]

from calculate import add
# 由内部tst调用外部caculate模块里的函数add，可以直接from，
# 因为from是基于项目下的目录进行寻找的，可以找到calculate
result = add(*list1)
print(result)  # 21

MAX = 1000