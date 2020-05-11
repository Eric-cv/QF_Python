# coding=utf-8
# @Time     :2020/4/9 0009 20:31
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func04.py
# @Software :PyCharm

'''
练习：
1.
def func(a, *args):
    print(a,args)

调用：
func(2,3,4,5)       2 (2 3,4,5)
func(2,[1,2,3,4])   2 ([1, 2, 3, 4],)
func(2,3,[1,2,3,4,5])   2 (3,[1, 2, 3, 4, 5])
func(5,6,(4,5,7),9)    5 (6, (4, 5, 7), 9)

2.
def func(a,b=10,c=3,**kwargs):   #关键字默认值
    print(a,b,c,kwargs)

func(1)       1 10 3 {}
func(2,b=10)  2 10 3 {}
func(3,5,7,a=1,b=2)   # TypeError: func() got multiple values for argument 'a'
# 正常应该给 a 3 b 5 c 7 然后关键字是 a=1 b=2
# 但是看到a=1时，会认为与之前的a 3冲突
func(3,5,7,x=1,y=2)  3 5 7 {'x': 1, 'y': 2}
func(3, c=5, b=7, x=1, y=2)  3 5 7 {'x': 1, 'y': 2}

3.
def func(a,*args, **kwargs):
    print(a,args,kwargs)

t=(1,2,3,4)
func(1,t)    1 ((1, 2, 3, 4),) {}

l=[2,5,8]
func(l,l,a=9,b=6)   TypeError: func() got multiple values for argument 'a'

func(l,l,c=9,b=6)  1 ([2, 5, 8],) {'c': 9, 'b': 6}
'''


def func(a, *args, **kwargs):
    print(a, args, kwargs)


l = [2, 5, 8]
dict1 = {'1': 'a', '2': 'b', '3': 'c'}
func(1, 2, 3, 4, 5, **dict1)  # func(1,2,3,4,5,1='a',2='b',3='c')

func(1, l, **dict1)
# 拆列表
func(1, *l, **dict1)  # func(1, 2, 5, 8, 1='a',2='b',3='c')


def func1(name, *args):
    if len(args) > 0:
        for i in args:
            print('{}学过了{}'.format(name, i))
    else:
        print('没有学过任何编程知识！')


course = ['html', 'mysql', 'python']

# 调用函数
func1('坤坤', *course)  # 拆列表，args装成元组

'''
无参数函数

def func():
    pass
    
有参数函数：
1.普通参数
    def func(name, age):
        pass
    func('aa',18) ----> 形参与实参的个数要一致
2.可变参数
   A.   def func(*args):
            pass
        func()     ----> 函数调用时，实参的个数可以没有，也可以多个  *不能是关键字参数
    
   B.   def func(**kwargs):
            pass 
        func(a=1,b=2)  -----> 函数调用时，实参的个数可以没有，也可以多个 *必须是关键字参数
   
   C.   def func(*args, **kwargs):
            pass
        
        list1 = [1,3,6,7,9]
        dict1 = {'1': 'a', '2': 'b'}
        func(*list, ** dict1)  # func(1,3,6,7,9,'1'='a','2'='b')
        
    D. 混用
        def func(name, *args, **kwargs):
            pass
        
        func('tom')  ----> 必须赋值
        
3.默认值
    def func(name, age=18):
        pass
    func('tom')    -----> tom 18
    func('tom',age=20)   ------> 关键字赋值
'''