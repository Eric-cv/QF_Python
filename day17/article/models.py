# coding=utf-8
# @Time     :2020/4/30 0030 20:57
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :models.py
# @Software :PyCharm

class Article:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def show(self):
        print('发表文章名字:{}的作者是：{}'.format(self.name, self.author))

class Tag:
    def __init__(self, name):
        self.name = name