# coding=utf-8
# @Time     :2020/4/24 0024 13:29
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :exception05.py
# @Software :PyCharm

# 抛出异常 raise
# 注册 用户名必须6位
def register():
    username = input('输入用户名：')
    if len(username) < 6:
        # 主动扔出一个Exception异常（类似系统报错，只不过是我们手动扔的）
        raise Exception('用户长度必须6位以上')
    else:
        print('输入的用户名是：', username)


try:
    register()
except Exception as err:  # 接住抛出的Exception异常
    print(err)
    print('注册失败！')
else:
    print('注册成功！')
