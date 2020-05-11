# coding=utf-8
# @Time     :2020/4/9 0009 19:51
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func03.py
# @Software :PyCharm


'''
使用函数的时候：
def aa(**kwargs):
    pass

a(a=1, b='hello',c = 'tom')   #
'''


def aa(**kwargs):
    print(kwargs)


aa(a=1, b='hello', c='tom')  # 装包: ['a': 1, 'b': 'hello', 'c': 'tom']

# 如果在开发的时候，已知一个字典
dict1 = {'a': 1, 'b': 'hello', 'c': 'tom'}
aa(**dict1)  # a=1, b='hello' , c='tom'   拆包的过程
# 只要调用的时候传两颗**就是拆包
# 只要定义的时候传两颗**就是装包


def bb(a,b,*c,**d):  # a,b是必须要有的，带*的是可有可无的
    print(a,b,c,d)

bb(1,2)   #  1  2 () {}
bb(1,2,3,4) #  1 2 (3,4) {}
bb(1,2,x=100,y=200)  # 1 2 () {'x':100, 'y':200}
bb(1,2,3,x=100)  # 1 2 (3,) {'x':100}
bb(1,2,x=100,5,6)
# 会报错，传的时候*c没有会跳过，默认后面都是关键字参数，
# 然后到了**d关键字参数发现不全是key=value形式，因此报位置错误
# 所以通常我们定义参数的时候都是按照上面的顺序，关键字参数放最后
# 即传入关键字参数后面就都得是关键字参数
bb(1,2,x=100,y=5,z=6)
