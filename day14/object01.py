# coding=utf-8
# @Time     :2020/4/25 0025 15:27
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :object01.py
# @Software :PyCharm
'''
面向对象：
程序    现实
对象 -->具体的事物
现实中事物-->转成电脑程序
世间万物皆对象

好处：

面向对象：
    类
    对象
    属性
    方法

对象：
    于鹏的手机
    小伟的手机
    赵飞的手机
    陈帅的手机
    ...

    对象的集合 --> 共同特征：品牌 颜色 大小 价格 动作：打电话 发短信 上网 游戏

    类别：手机类

         学生类
    于鹏，小伟，赵飞，陈帅...
    特征：姓名 年龄 性别 身高 血型 婚否  ---->属性
    动作：刷抖音 敲代码 看书...     ---->方法

    多个对象 ----> 提取对象的共同特征和动作 ---->封装到一个类中

'''
# 所有的类名要求首字母大写，多个单词使用驼峰式命名
# ValueError TypeError StopIterable
# 默认继承object
'''
class 类名[(父类)]:
    属性： 特征
    
    方法： 动作

'''


class Phone:
    # 属性
    brand = 'huawei'

    # 方法


print(Phone)  # <class '__main__.Phone'>
# 使用类创建对象
yp = Phone()
print(yp)  # <__main__.Phone object at 0x000001D47F2F6A58>
print(yp.brand)
yp.brand = 'iphone'  # 改一下品牌
print(yp.brand)

feifei = Phone()
print(feifei)  # <__main__.Phone object at 0x000001D47F301550>
print(feifei.brand)
feifei.brand = 'iphone xxs'
print(feifei.brand)

xiaowei = Phone()
print(xiaowei.brand)

