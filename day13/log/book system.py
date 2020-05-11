# coding=utf-8
# @Time     :2020/4/23 0023 10:55
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :book system.py
# @Software :PyCharm

# 持久化保存： 文件
# list: 元组，字典 ---> 内存 （这都不属于持久化的）

# 用户注册

# def register():
#     username = input('输入用户名：')
#     password = input('输入密码：')
#     repassword = input('输入确认密码：')
#
#     if password==repassword:
#         # 保存信息
#         with open(r'E:\Files_plus\Project01\QF_Python\day13_test\p2\books\users.txt', 'a') as wstream:
#             wstream.write('{}, {}\n'.format(username, password))
#
#         print('用户注册成功！')
#     else:
#         print('密码不一致！')

# 用户登录
# def login():
#     username = input('输入用户名：')
#     password = input('输入密码：')
#     if username and password:
#         with open(r'E:\Files_plus\Project01\QF_Python\day13_test\p2\books\users.txt', 'r') as rstream:
#             while True:
#                 user = rstream.readline()  # admin 123456\n
#                 # 终止条件，全部遍历完毕都没有找到输入用户
#                 if not user:
#                     print('用户名或者密码输入有误！')
#                     break
#
#                 input_user = '{}, {}\n'.format(username, password)
#                 if user == input_user:
#                     print('用户登录成功！')
#                     break

def show_books():
    print('------图书馆里的图书有------')
    with open(r'E:\Files_plus\Project01\QF_Python\day13_test\p2\books\books.txt', 'rb') as rstream:
        books = rstream.readlines()
        for book in books:
            print(book.decode('utf-8'), end='')

# 调用函数
#register()
#login()
show_books()

