'''
字符串中可以使用的符号
+ 
*
in
not in 
is
not is
[]
'''

'''
列表中支持的符号
+
*
in

'''
l1 = [1, 2, 3]
l2 = [5, 6, 7]

l3 = l1 + l2
print(l3)

l4 = [5, 8 ]*3
print(l4)

result = 3 in [1, 2, 3, 4] # True
print(result)

result = [3] in [1, 2, 3, 4] # False
print(result)

result = [3] in [1, 2, [3], 4] # True
print(result)
'''
列表中元素：
整型
字符串类型
浮点型
列表
元组
字典
对象
[[....], [....], [....], [....] ]
'''
# [1, 2, 3, 'aa', 'bb', [1, 2], [6, 8, 9, 0]]

l5 = [[1,2],[3,2,1],[4,5]]

print(len(l5))  # 3

e = l5[2]
print(e, type(e))  # [4, 5]

print(e[1])

print(l5[1][1])

print(l5[2][1])

print(range(1, 10 ,3)) # 1, 4 ,7 


'''
类型转换
str()
int()
list()  # 将指定内容转成列表，可迭代的内容可以放到list中

s = 'abc'
result = list(s)  # ['a', 'b', 'c']

iterable 可迭代的  for in 里面可以循环就是可迭代的
'abcdef' ----> ab c
for i in range(5):
	pass

'''
print(list(range(1,10,3)))  # [] 

s = 'abc'
result = list(s)
print(result)

#result = list(10)  # int is not iterable迭代
#print(result)



s1 = 'this is a test of python'
print(s1.find('test'))

a= 'aa26dVC8DsvRLF5D45'

S=''
for i in a:
	if i.isupper():
		S+=i.lower()
	elif i.islower():
		S+=i.upper()
	else:
		S+=i
print(S)
