# coding=utf-8
# @Time     :2020/4/30 0030 16:52
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :module01.py
# @Software :PyCharm
'''
在python中，模块是代码组织的一种方式，把功能相近的函数或者类放到一个文件中，一个文件(.py)就是一个模块
这样做的好处是：
-提高了代码的可复用、可维护性。一个模块编写完毕后，可以很方便的在其他项目中导入
-解决了命名冲突，不同模块中相同的命名也不会冲突

1.自定义模块
2，使用系统的一些模块

导入模块：
1.import 模块名
  在代码中可以使用：模名块.变量       模名块.函数      模名块.类
2.from 模块名 import 变量  函数  类
  在代码中可以直接使用：变量，函数，类
3.from 模块名 import *
  该模块中所有内容
  但是如果想限制获取的内容，可以在模块中使用__all__ = [使用*可以访问到的内容]
4.无论是import还是from的形式，都会对模块中所有的内容进行一个加载
  如果不希望其进行调用，就会用到__name__
  在自己的模块里面，__name__叫:__main__
  如果在其他模块中通过导入的方式调用的话：__name__: 模块名
'''
# # 导入模快 import 模块名
# import calculate
#
# # 使用模块中的函数，模块名.变量，   模块名。类
# list1 = [4, 2, 7, 8, 9]
#
# # *list1把列表拆包
# result = calculate.add(*list1)
# print(result)
#
# # 使用模块变量
# print(calculate.number)
# # 使用模块中的类
# cal = calculate.Calculate(88)
# cal.test()
# calculate.Calculate.test1()

# from calculate import add, number, Calculate
from calculate import *


list1 = [4, 2, 7, 8, 9]
result = add(*list1)
print(result)

sum = result + number
print(sum)

c = Calculate(80)
test()