# coding=utf-8
# @Time     :2020/4/30 0030 16:06
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :singleton.py
# @Software :PyCharm

# 单例模式：
# 开发模式：单例模式：对内存的一种优化，创建多个对象时，都采用同一个地址空间
# 创建新对象时，判断存地址的私有化变量__instance是不是空，如果是空，就创建新地址，
# 不是空，就把原来的地址拿出来给新对象作为地址

class Student:
    pass


s = Student()
s1 = Student()
s2 = Student()
print(s)  # <__main__.student object at 0x0000027605b96048>
print(s1)  # <__main__.Student object at 0x0000027605ED6A58>
print(s2)  # <__main__.Student object at 0x0000027605ED6A20>


class Singleton:
    # 私有化 单例的地址就存在于__instance
    __instance = None
    name = 'jack'
    # 重写父类__new__
    def __new__(cls):
        # print('------> __new__')
        if cls.__instance is None:
            # print('---->1')
            cls.__instance = object.__new__(cls)
            # print(cls.__instance)
            # 这里是return给__init__，虽然此处没定义__init__，__init__之后赋值给对象s，开辟空间
            return cls.__instance
        else:
            # print('---->2')
            return cls.__instance

    def show(self, n):
        print('-------->show', Singleton.name, n)

s = Singleton()
s1 = Singleton()
# print(dir(Singleton))

print(s)  # <__main__.Singleton object at 0x0000026659233F28>
print(s1)  # <__main__.Singleton object at 0x0000026659233F28>

s.show(5)  # -------->show jack 5
s1.show(7)  # -------->show jack 7