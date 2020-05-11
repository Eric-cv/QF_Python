# coding=utf-8
# @Time     :2020/4/8 0008 23:58
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func02.py
# @Software :PyCharm

# 可变参数 + 关键字参数
# 关键字参数：key=value


def add(a, b=10):  # 关键字参数，此时的b是默认值
    result = a + b
    print(result)


# 调用
add(5)
add(4, 7)  # a=4 , b=7，此时7就会覆盖原来b的默认值


def add1(a, b=10, c=4):
    print(a, b, c)
    result = a + b + c
    print(result)


add1(1)

add1(1, 5)  # 是给b赋值成功

# 给c赋值而不是给b赋值
add1(2, 6)  # 默认6是赋值给b了
add1(2, c=6)  # 如果想将6赋值给c，则需要结合关键字的key使用

# 函数，计算每位同学姓名和年龄
students = {'001': ('蔡徐坤', 21), '002': ('王源', 19), '003': ('王俊凯', 20), '004': ('易烊千玺', 19)}


def print_boys(name, persons):  # persons = students
    if isinstance(persons, dict):
        values = persons.values()
        print(values)
        for name, age in values:
            print('{}的年龄是：{}'.format(name, age))


# 调用
print_boys('蕊蕊', students)


def func(**kwargs):  # key word argument
    print(kwargs)


# 关键字参数，调用
func()  # {}
func(a=1)  # {'a':1}
func(a=1, b=2, c=3)  # {'a':1,'b':2,'c':3}
# **kwargs就说明，只要外面给函数送值，送的值必须是key=value，系统会默认把送的值作为字典保存

dict1 = {'001': 'python', '002': 'java', '003': 'c语言', '004': 'go'}
# func(dict1)   # 字典为一个整体，不属于关键字参数，不符合key=value
func(**dict1)  # 传递实参：**变量名(**只能接字典)，将字典进行拆包，
# 步骤：
# 1.将字典进行拆包，拆成关键字参数的形式：func('001'='python', '002'='java'...)
# 2.func里面的参数都是关键字参数
# 3.将关键字参数再进行一次装包动作
# 4.装包成功：kwargs就是装包成功的字典

