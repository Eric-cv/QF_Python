# coding=utf-8
# @Time     :2020/4/25 0025 17:24
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :object01.py
# @Software :PyCharm

# 类中方法：动作
# 种类：普通方法 类方法 静态方法 魔术方法
'''
普通方法格式：
def 方法名(self[,参数,参数]):
    pass

'''


class Phone:
    brand = 'xiaomi'
    price = 4990
    type = 'mate 80'

    # Phone类里面普通方法 call
    def call(self):
        print('self------->', self)
        print('正在访问通讯录：')
        for person in self.address_book:  # [{}, {}]
            print(person.items())
        print('正在打电话...')
        print('留言：', self.note)


phone1 = Phone()
phone1.note = '我是phone1的note'
phone1.address_book = [{'15900886745': '于鹏'}, {'15900880000': '小伟'}]

# <__main__.Phone object at 0x000002C80D0018D0> ----1-----
print(phone1, '----1-----')
# self-------> <__main__.Phone object at 0x000002C80D0018D0>
phone1.call()  # call(phone1) ----> self.note

print('***********')

phone2 = Phone()
phone2.note = '我是phone2的note'
# <__main__.Phone object at 0x000002C80D001978> ----2-----
print(phone2, '----2-----')
# self-------> <__main__.Phone object at 0x000002C80D001978>
phone2.call()  # call(phone2)----> self.note
