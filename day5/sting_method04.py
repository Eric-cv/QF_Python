# isalpha() 是否是字母 isdigit()是否是数字
s = 'abcd'
result = s.isalpha()
print('result=',result)

s = '6688'
result = s.isdigit()
print('result=',result)

sum=0
for i in range(3):
	num = input('请输入数字：')  # 11
	
	if num.isdigit():
		num = int(num)
		sum+=num

print('sum',sum)



sum = 0
i = 1
while i <= 3:
	num = input('请输入数字：'):

	if num.isalpha():
		num = int(num)
		sum+=sum
		print('第{}个数字累加成功！'.format(i))
		i+=1
	else:
		print('不是数字！')

print('sum',sum)


# join(): '-'.join('abc')  将abc用-连接构成一个新的字符串
new_str = '-'.join('abc')
print(new_str)


# python 列表  list=['a','v','o','9']数组
list1 = ['a','v','o','9']
result = ''.join(list1)
print(result)

result = ' '.join(list1)
print(result)

# lstrip
s= '     hello    '
s= s.lstrip() # 去除字符串左侧的空格
print(s+'8')

s= '     hello    '
s= s.rstrip() # 去除字符串右侧的空格
print(s+'8')

s= '     hello    '
s= s.strip() # 去除字符串的空格
print(s+'8')

# split('分隔符',次数) 分割字符串，将分割后的字符串保存到列表中
s = 'hello world hello kitty'
result = s.split(' ')
print(result)
result = s.split(' '，2)
print(result)

# count(args) 求字符串中指定args的个数
n = s.count(' ')
print('个数',n)





