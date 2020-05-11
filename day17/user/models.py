# coding=utf-8
# @Time     :2020/4/30 0030 20:57
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :models.py
# @Software :PyCharm
__all__ = ['User']  # 只是针对from 包.模块 import * 起作用

version = '1.1'


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if username == self.username and password == self.password:
            print('登陆成功')
        else:
            print('登陆失败')

    def publish_article(self, article):
        print(self.username, '发表了文章', article.name)

    def show(self):
        print(self.username, self.password)

# print(__name__)
# if __name__ == '__main__':
#     print('------user------')
