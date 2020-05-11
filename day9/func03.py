# coding=utf-8
# @Time     :2020/4/3 0003 13:29
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func03.py
# @Software :PyCharm

'''
定义一个登陆函数，参数是：username, password
函数体：
判断参数传过来的username,password是否正确，如果正确则登陆成功，否是打印登陆失败
'''


def login(username, password):
    # 相当于数据库注册的用户名和密码
    uname = 'admin123'
    pwd = '112233'

    for i in range(3):

        if username == uname and password == pwd:
            print('登陆成功!')
            break
        else:
            print('登陆失败！')
            username = input('请输入登陆用户名：')
            password = input('输入密码：')
    else:
        print('账户锁定！')


# 调用：
username = input('请输入登陆用户名：')
password = input('输入密码：')
login(username, password)
