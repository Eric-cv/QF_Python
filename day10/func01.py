# coding=utf-8
# @Time     :2020/4/4 0004 0:34
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func01.py
# @Software :PyCharm

#  可变参数
def add(a, b):
    pass


add(1, 3)


# 定义方式：
def add(*args):  # arguments 参数声明
    #  print(args)
    sum = 0
    if len(args) > 0:
        for i in args:
            sum += i
            print('累加的和', sum)
    else:
        print('没有元素可计算', sum)


add()  # 空元组
add(1)  # (1,)
add(1, 2)  # (1,2)
add(1, 2, 3)  # (1,2,3)
add(1, 2, 3, 4)  # (1,2,3,4)


# xxx计算出的累加和是：xxx

def add(name, *args):  # arguments 参数声明
    print(args, name)
    sum = 0
    if len(args) > 0:
        for i in args:
            sum += i
            print('%s累加的和是：%s' % (name, sum))
    else:
        print('没有元素可计算', sum)


# 调用
add('飞飞', 4, 6, 8)
# a, *b = 1,3,5,6,7
# 注意：可变参数必须放在后面

