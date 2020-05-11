# coding=utf-8
# @Time     :2020/4/25 0025 13:59
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :generator04.py
# @Software :PyCharm

# 进程>线程>协程
def task1(n):
    for i in range(n):
        print('正在搬第{}块砖'.format(i))
        yield None  # 只暂停，不扔值


def task2(n):
    for i in range(n):
        print('正在听第{}首歌'.format(i))
        yield None  # 只暂停，不扔值


g1 = task1(5)
g2 = task2(5)

while True:
    try:
        g1.__next__()
        g2.__next__()
    except:
        break

'''
生成器：generator
定义生成器方式：
1.通过列表推导式方式
    g=(x+1 for x in range(6))
2.函数+yield
    def fun():
        ...
        yield
    g = func()
    
    产生元素：
    1.next(g)  # 每次调用都会产生一个新的元素，如果元素产生完毕，再次调用会产生异常
    2.生成器自己的方法：
        g.__next__()
        g.send(value)
    应用：携程
'''
