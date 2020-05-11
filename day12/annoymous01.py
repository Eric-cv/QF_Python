# coding=utf-8
# @Time     :2020/4/15 0015 23:38
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :annoymous01.py
# @Software :PyCharm

# 匿名函数:简化函数定义
# 格式：lambda 参数1，参数2... : 运算(return 返回的结果)

def func():
    print('aaaa')


def add(a, b):
    s = a + b
    return s


f = add

s = lambda a, b: a + b
print(s)  # s就是函数function
result = s(1, 2)  # 把1,2的值作为参数给了a，b，进行运算a+b并返回给s
print(result)

s = lambda x, y: x * y
result = s(2, 5)
print(result)


# 匿名参数作为参数
def func(x, y, func):
    print(x, y)
    print(func)
    func(x, y)
    s = func(x, y)
    print(s)


# 调用func
# func我传了参数1和2，第三参数我想传入一个求和函数，但是我又不想单独定义，
# 因此采用匿名函数，求a，b的和

func(1, 2, lambda a, b: a + b)

# 匿名函数与内置函数的结合使用
# max sorted zip...

list1 = [3, 5, 8, 9, 0]
m = max(list1)
print('列表的最大值：', m)
list2 = [{'a': 10, 'b': 20}, {'a': 13, 'b': 20}, {'a': 9, 'b': 20}, {'a': 29, 'b': 20}]
m = max(list2, key=lambda x: x['a'])
print('列表的最大值：', m)

