'''
str()
int()
len()
list()
sorted()
print()
input()
enumerate() # 列举，枚举
            # 函数用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列

'''

l1 = ['a', 'abc', 'jk', 'opop']

# enumerate(l1) ---> index value

for index, value in enumerate(l1):
	print(index, value)


for index, value in enumerate('happy'):
	print(index, value)

# 算法
# 冒泡排序
# 系统自带
numbers = [5,7,8,9,2,0,6,4,9]
numbers = sorted(numbers)
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# 手写冒泡
numbers = [8,5,9,7]

for i in range(len(numbers)):
	# numbers[i] = 5
	for j in range(i+1, len(numbers)):
		if numbers[i]>numbers[j]:
			# 快速交换
			numbers[i], numbers[j] = numbers[j], numbers[i]
			
			print(numbers)
	print('-------->', i)
# 手写选择
mylist = [4, 1, 7, 0]

for i in range(length(mylist)-1):
	# 每一轮的比较，注意range1的变化，这里需要进行length-1长度的比较，注意-i的意义（可以比较已经排好序的元素）
	for j in range(0, length-1-i):
		# 交换
		if mylist[j] > mylist[j+1]:
			mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

print(mylist)


