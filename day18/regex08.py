# coding=utf-8
# @Time     :2020/5/1 0001 23:50
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :regex08.py
# @Software :PyCharm
import re

# 分组
# 匹配数字0-100数字
n = '89'
'''
 | 或者
'''
result = re.match(r'[1-9]?\d?$|100$', n)  # ？表示前面的模式可以有可以没有
print(result)

# (word|word|word)  区别  [abc] 表示的是一个字母而不是一个单词
# 验证输入的邮箱 163 126 qq
email = '738473800@qq.com'
result = re.match(r'\w{5,20}@(163|126|qq)\.(com|cn)$', email)
print(result)

print('--------------')
# 不是以4、7结尾的手机号码（11位）
phone = '15901018869'
result = re.match(r'1\d{9}[0-35-689]$', phone)
print(result.group())  # 15901018869

#  爬虫
phone = '010-12345678'
result = re.match(r'(\d{3}|\d{4})-(\d{8}$)', phone)
print(result)  # <re.Match object; span=(0, 12), match='010-12345678'>
# 分别提取
print(result.group())  # 010-12345678
# ()表示分组，gruop(1)表示提取到第一组的内容，gruop(2)表示提取到第二组的内容，
print(result.group(1))  # 010
print(result.group(2))  # 12345678

#
msg = '<html>abc</html>'
msg1 = '<h1>hello</h1>'
result = re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>$', msg)
print(result)
print(result.group())  # <html>abc</html>
print(result.group(1))  # abc

# number
result = re.match(r'<([0-9a-zA-Z]+)>(.+)</\1>$', msg1)
print(result)  # <re.Match object; span=(0, 14), match='<h1>hello</h1>'>
print(result.group(1))  # h1
print(result.group(2))  # hello

msg = '<html><h1>abc</h1></html>'
result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$', msg)
print(result)  # <re.Match object; span=(0, 25), match='<html><h1>abc</h1></html>'>
print(result.group(1))  # html
print(result.group(2))  # h1
print(result.group(3))  # hello
