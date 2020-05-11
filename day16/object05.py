# coding=utf-8
# @Time     :2020/4/29 0029 15:12
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :object05.py
# @Software :PyCharm
# student book student
'''
1. has a
    一个类中使用了另外一种自定义类型
    student使用computer books
2.类型
    系统类型：
    str int float
    list dict tuple set
    自定义类型：
    自定义的类都可以将其当成一种类型
    s = Student()
    s 是Student类型的对象
'''

class Computer:

    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def online(self):
        print('正在使用电脑上网...')

    def __str__(self):
        return self.brand + '-----' + self.type + '---' + self.color


class Book:
    def __init__(self, bname, author, number):
        self.bname = bname
        self.author = author
        self.number = number

    def __str__(self):
        return self.bname + '---' + self.author + '---' + int(self.number)


class Student:  # has a
    def __init__(self, name, computer, book): # compuer和book的是按对象传入的
        self.name = name
        self.computer = computer
        self.books = []
        self.books.append(book)  # 把book对象传入books列表中

    def borrow_book(self, book):  # book就是一个book对象
        for book1 in self.books:
            if book1.bname == book.bname: # 比较拥有的book和借来的book是否重复
                print('已经借过此书！')
                break
        else:
            # 将book对象加入到列表中
            self.books.append(book)
            print('添加成功！')
    def show_book(self):
        for book in self.books:  # book就是一个book对象
            print(book.bname)

    def __str__(self):
        return self.name + '---' + str(self.computer) + '---' + str(self.books)


# 创建对象
computer = Computer('mac', 'mac_pro_2018', '深灰色')
book = Book('盗墓笔记', '南派三叔', 10)
stu = Student('songsong', computer, book)
print(stu)

# 看借了哪些书
stu.show_book()

# 再借一本鬼吹灯
book1 = Book('鬼吹灯', '天下霸唱', 8)
stu.borrow_book(book1)

# 看借了哪些书
print('-------------')
stu.show_book()
