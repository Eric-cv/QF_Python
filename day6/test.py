#

if 'good' == 'good':  # == 比较的是内容
	print('相等')

if 'good' in 'good': # in 运算符 应用在字符串判断中，也可是用于列表
	print('相等或者包含')


i=1

if 'good' in ['goods','good','abc','aaaa']:
	print('包含....',i)
	i+=1
# >>> 包含....1

for w in ['goods','good','abc','aaaa']:
	print('good' in w)
	print('------>',i)
	i+=1
# >>> True   1   True   2   False   3    False    4

'''
if 可以让 in 判断作为一个条件表达式
	if 'a' in 'abc':
		pass
	if 'a' in ['a','b','c']:
		pass

但是：
for ... in  循环条件

for 变量 in 字符串列表：
	pass


'''
