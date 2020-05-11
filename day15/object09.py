# coding=utf-8
# @Time     :2020/4/26 0026 22:37
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :object09.py
# @Software :PyCharm


# __str__
# 触发时机：打印对象名 自动触发去调用__str__里面的内容
# 注意：一定要在__str__方法中添加return, return后面的内容就是打印对象看到的内容
class Person:
    def __init__(self, name):
        self.name = name
        self.age = age

    def __str__(self):
        return '姓名是' + self.name + str(self.age)


# 单纯打印对象名称，出来的是一个地址。地址对于开发者来说没有意义
# 如果想在打印对象名的时候给开发者更多的一些信息量，
p = Person('tom', 20)
print(p)


'''
总结：魔术方法
重点：
    __init__   <构造方法，创建完空间后调用的第一个方法>  
    __str__
了解：
    __new__   作用：开辟空间   
    __del__   作用：没有指针引用的时候会调用，99%都不需要重写。
    __call__  作用：想不想将对象当成函数用
    
    
大总结：
方法：
    普通方法  ---> 重点
        def 方法名(self, 参数):
            方法体
            
        调用：
        对象.方法名()
        方法之间的调用：
        class A:
            def a(self):
                pass
            def b(self):
                # 调用a方法
                self.a()
                
    类方法:  
        @classmethod
        def 方法名(cls[,参数...]):
            pass
        调用：
        类名.方法名()
        对象.方法名()
    静态方法：
        @staticmethod
        def 方法名([参数...]):
            pass
        调用：
        类名.方法名()
        对象.方法名()
    魔术方法:
        自动执行方法
'''