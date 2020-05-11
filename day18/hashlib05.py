# coding=utf-8
# @Time     :2020/5/1 0001 15:35
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :hashlib05.py
# @Software :PyCharm

# 加密算法 md5 sha1 sha256 不可逆
# base64 可逆
import hashlib

msg = ' 于鹏中午一起吃饭去！'
md5 = hashlib.md5(msg.encode('utf-8'))
print(md5.hexdigest())  # 16进制加密：287afeefebf5e57d435657276cecec85

sha1 = hashlib.sha1(msg.encode('utf-8'))
print(sha1.hexdigest())  # 47b344f9bc7ceebbf22f6e6f2b55ba4d39b4402a

sha256 = hashlib.sha256(msg.encode('utf-8'))
print(sha256.hexdigest())  # f94fec0ba1072843178e0f13a38ab36c36800b4b12c5039aff85f62d1deef217

# case:
password = '123456'
list1 = []
sha256 = hashlib.sha256(password.encode('utf-8')).hexdigest()
list1.append(sha256)

pwd = input('输入密码：')
pwd = hashlib.sha256(pwd.encode('utf-8')).hexdigest()
# print(pwd)
for i in list1:
    if pwd == i:
        print('登陆成功！')
    else:
        print('密码输入错误！')
