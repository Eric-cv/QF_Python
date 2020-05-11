# coding=utf-8
# @Time     :2020/5/2 0002 10:42
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :regex09.py
# @Software :PyCharm
import re
# 为分组起名，后面匹配的时候直接调用名字
# 起名的方式：(?P<名字><正则> (?P=名字))
msg = '<html><h1>abc</h1></html>'
result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>$', msg)
print(result)  # <re.Match object; span=(0, 25), match='<html><h1>abc</h1></html>'>
print(result.group(1))  # html
print(result.group(2))  # h1
print(result.group(3))  # abc

'''
    分组：()  ---->  result.group(1)  获取组中匹配的内容，
          在分组的时候，还可以结合|使用
            #  爬虫
            phone = '010-12345678'
            result = re.match(r'(\d{3}|\d{4})-(\d{8}$)', phone)
            print(result)  # <re.Match object; span=(0, 12), match='010-12345678'>
            # 分别提取
            print(result.group())  # 010-12345678
            # ()表示分组，gruop(1)表示提取到第一组的内容，gruop(2)表示提取到第二组的内容，
            print(result.group(1))  # 010
            print(result.group(2))  # 12345678

    不需要引用分组的内容：
        result = re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>$', msg)
        print(result)
        print(result.group())  # <html>abc</html>
        print(result.group(1))  # abc
    引用分组匹配的内容：
        1.number  \number 引用第number组的数据
            msg = '<html><h1>abc</h1></html>'
            result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$', msg)
            print(result)  # <re.Match object; span=(0, 25), match='<html><h1>abc</h1></html>'>
            print(result.group(1))  # html
            print(result.group(2))  # h1
            print(result.group(3))  # hello
        2.?P<名字>
            msg = '<html><h1>abc</h1></html>'
            result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>$', msg)
            print(result)  # <re.Match object; span=(0, 25), match='<html><h1>abc</h1></html>'>
            print(result.group(1))  # html
            print(result.group(2))  # h1
            print(result.group(3))  # abc

    re模块：
    match   从开头匹配，匹配一次
    search  只匹配一次
    findall  查找索引
    sub(正则表达式, '新内容', string)  替换
    split result = re.split(r'[,:]', 'java: 99, python:95')
    在字符串总搜索，如果遇到','或者':'就分割，将分割的内容都保存到列表中
'''


#   sub(正则表达式, '新内容', string)  替换
result = re.sub(r'\d+', '90', 'java: 100, python:100')
print(result)  # java: 90, python:90


def func(temp):
    num = temp.group()
    num1 = int(num) + 1
    return str(num1)

result = re.sub(r'\d+', func, 'java: 99, python:95')
print(result)  # java: 100, python:96

# split 切割
result = re.split(r'[,:]', 'java: 99, python:95')
print(result)  # ['java', ' 99', ' python', '95']
