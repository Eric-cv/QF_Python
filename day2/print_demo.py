# print函数
# 1.用法
print('hello world')
name = '小白'
print(name)

# 2.用法：print(name ,age, gender)
age = 18
gender = 'boy'

# 3.用法：print(value, value, value,....., sep = ' ', end = '\n')
print(name, age, gender)  # sep默认的分隔符是空格
print(name, age, gender, sep='#') #sep = '*'  

# 转义字符：\n  换行
print('hello\nkitty')
print('AAA', end='')  #'AAA\n'  ----> 'AAA'
print('BBB', end='')  #'BBB\n'  ----> 'BBB'
print('BBB', end='')  #'CCC\n'  ----> 'CCC'

# 练习: 亲爱的xxx：
      #     请点击链接激活用户：激活用户
print()
print('亲爱的xxx：\n', '\t请点击链接激活用户：激活用户')

# 转义字符： \n 换行  \t 制表符  \'  \"  \r 回车  \\
print('乔治说：\' 想吃冰淇淋！\'') 
print("乔治说：\" 想吃冰淇淋！\"")
# 测试 ‘‘’’   “ ‘ ’ ”    ‘ “ ” ’   
# print('乔治说： '想玩恐龙！'')  # 错
print("乔治说： '想玩恐龙！'")
print('乔治说： "想睡觉！"')

print('\哈哈哈哈')
print('\hahahaha')
print('\\hahahaha')
print('hello\py\thon')
print('hello\py\\thon')
print(r'hello\py\thon')  # r''  raw 原样输出字符串内容，即使有转义字符也不转义
