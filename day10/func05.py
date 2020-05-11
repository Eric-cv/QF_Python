# coding=utf-8
# @Time     :2020/4/9 0009 21:49
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func05.py
# @Software :PyCharm

# 返回值: 将函数中运算的结果通过return关键字 '扔'出来

'''
def add(a, b):
    result = a + b
    print(result)  # 仅仅限于打印在终端上，辅助查看，但是外部是无法使用的
    return 'hello', 100, 9


# 调用函数
x = add(2, 6)
print(x)
x, *y = add(2, 6)
print(x, *y)

'''

'''
return 返回值
1.return后面可以是一个参数，接收的时候x = add(1,2)
2.return后面也可以是多个参数，如果是多个参数底层会将多个参数保存在元组中
  将元组作为整体返回  x = add(1,2)  x ---> (1,2,3)
3.接收的时候也可以是多个： return 'hello','world'  x,y = ('hello','world')

'''
