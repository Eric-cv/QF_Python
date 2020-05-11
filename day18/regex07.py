# coding=utf-8
# @Time     :2020/5/1 0001 21:18
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :regex07.py
# @Software :PyCharm

# qq = input('输入qq号码')
# if len(qq) >= 5 and qq[0] != 0:
#     print('合法的')
# else:
#     print('不合法的')


import re

msg = '佟丽娅娜扎热巴代斯'
pattern = re.compile('佟丽娅')
result = pattern.match(msg)  # 没有匹配
print(result)  # <re.Match object; span=(0, 3), match='佟丽娅'>

# 使用正则re模块方法：match
s = '娜扎佟丽娅热巴代斯'
result = re.match('佟丽娅', s)  # 只要从开头进行匹配，如果匹配不成功则就返回None
print(result)  # None

# search
result = re.search('佟丽娅', s)  # search 进行正则字符串匹配方法，匹配的是整个字符串
print(result)  # <re.Match object; span=(2, 5), match='佟丽娅'>
print(result.span())  # (2, 5) 返回匹配的位置
print(result.group())  # 佟丽娅  使用group提取匹配的内容部分
print(result.groups())


s = '哈哈1'
result = re.search('[0-9]', s)
print(result)  # <re.Match object; span=(2, 3), match='1'>

s = '哈哈3a'
result = re.search('[0-9][a-z]', s)
print(result)  # <re.Match object; span=(2, 4), match='3a'>

# a2b h6k
msg = 'abcd7yjkfd8hdf00'

result = re.search('[a-z][0-9][a-z]', msg)
print(result.group())  # d7y  search只有有匹配的后面就不会继续进行检索，找到一个匹配就会暂停

result = re.findall('[a-z][0-9][a-z]', msg)  # findall匹配整个字符串，找到一个继续向下找一直到字符串的结尾
print(result)  # ['d7y', 'd8h']

# 正则符号
# a7a a88a a7788a
msg = 'a7aopa88akjgka7878a'
result = re.findall('[a-z][0-9]+[a-z]', msg)  # ’+‘代表出现大于等于1次
print(result)  # ['a7a', 'a88a', 'a7878a']

# qq号码验证 5~11 开头不能是0
qq = '1494468962'
result = re.match('^[1-9][0-9]{4,10}$', qq)
print(result)

# 用户名可以是字母或者数字下划线，不能是数字开头，用户名长度必须6位以上
username = 'admin001'
result = re.search('^[a-zA-Z]\w{5,}$', username)
print(result)  # <re.Match object; span=(0, 8), match='admin001'>
# 注意：如果是验证整个用户名是否匹配正则的格式，那需要在正则的格式中前面加’^‘，后面加’$‘
# 否则可能会得到中间匹配的结果，^ - $代表从字符的开头到字符的结尾作为整体去跟正则格式匹配

msg = 'aa*py ab.txt bb.py kk.png uu.py apyb.txt'
result = re.findall(r'\w+\.py\b', msg)
print(result)
'''
    总结：
    .  任意字符除(\n)
    ^  开头
    $  结尾
    [] 范围  [abc]  [a-z]  [a-z*&￥]
    
    正则预定义：
    \s  空白  （空格）
    \b  边界
    \d  数字
    \w  word [0-9a-zA-Z_]
    
    大写： 
    \S  非空格
    \D  非数字
    ’\w[0-9]‘  ---> \w [0-9] 只能匹配一个字母
    
    量词：
    *  >= 0
    +  >= 1
    ?  0, 1
    
    手机号码的正则
    re.match('1[38579]\d{9}$', phone) 
    
    {m}     固定m位
    {m, }   >= m位
    {m, n}  >= m , <= n 位

'''











