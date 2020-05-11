# coding=utf-8
# @Time     :2020/4/15 0015 21:35
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func12.py
# @Software :PyCharm

# 开发：登陆验证
import time

islogin = False # 默认是没有登录的

# 定义一个login函数
def login():
    username = input('输入用户名')
    password = input('输入密码')
    if username == 'admin' and password == '123456':
        return  True
    else:
        return  False


# 定义一个装饰器，进行付款验证
def login_required(func):
    def wrapper(*args, **kwargs):
        global islogin
        print('-------付款---------')
        # 验证用户是否登录
        if islogin:
            func(*args, **kwargs)
        else:
            # 跳转到登录页面
            print('用户没有登录，不能付款！')
            islogin = login()
            print('result:', islogin)

    return wrapper


@ login_required
def pay(money):
    print('正在进行付款，付款金额是：{}元'.format(money))
    print('付款中')
    time.sleep(2)
    print('付款完成')


# 调用付款
pay(10000)

pay(8000)