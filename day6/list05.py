# list列表的添加
# 临时小数据库：list 
# 创建一个空列表

girls=['杨幂']

# quit  表示退出

# 列表的函数使用: append  extend insert

# append()  末尾追加
while True:

	name = input('请输入你心目中的美女名字：\n')
	if name == 'quit':
		break
	girls.append(name)

print(girls)

# extend  类似列表的合并
girls=['杨幂']
names = ['黑嘉嘉','孙俪','巩俐','王丽坤']

#name = input('请输入你心目中的美女名字：\n')
girls.extend(name)

print(girls)

# 符号 +  也可以用于列表的合并

girls = girls + names
print(girls)

# append 末未追加
# insert 指定位置插入
# expend 一次添加多个元素

# [杨幂',黑嘉嘉','孙俪','巩俐','王丽坤']
#   0     1       2      3      4
girls.insert(1,'刘涛')

print(girls)

# 产生10个随机数，将其保存到列表中
'''
步骤：
1.如何产生随机数
2.10个数字产生
3.将产生的随机数放到列表中
4.打印列表
'''
import random

random_list = []  # 存放随机数

for i in range(10):
	
	ran = random.randint(1,50)
	# 保存到列表中
	random_list.append(ran)

print(random_list)



# 产生10个不同的随机数，将其保存在列表中

# for方法，个数不一定是10个
random_list = []

for i in range(10):
	
	ran = random.randint(1,50)
	
	#if ran in random_list:
	#	pass	
	#else:
	#	random_list.append(ran)
	if ran not in random_list:
		random_list.append(ran)

print(random_list)

# while 方法
random_list = []

i =0

while i<10:
	ran = random.randint(1,20)
	if ran not in random_list:
		random_list.append(ran)
		i+=1

print(random_list)


# 找出列表中的最大\小值  max(list)  ---->列表中的最大、小值

random_list = []

i =0

while i<10:
	ran = random.randint(1,20)
	if ran not in random_list:
		random_list.append(ran)
		i+=1

max_value = max(random_list)
min_value = min(random_list)
print(random_list)
print(max_value)
print(min_value)


# 自定义求最大\小值
# 假设列表中的第一个元素就是最大值
mvalue = random_list[0]
min_value = random_list[0]

for value in random_list:
	# 求最大值
	if value > mvalue:
		mvalue = value
	# 求最小值
	if value < min_value:
		min_value = value

print('最大值是：',mvalue)
print('最小值是：',min_value)

# 求和
# 系统函数求和
he = sum(random_list)
print('系统计算求和：',he)

# 手写求和
for value in random_list:
	sum_1 += value

print(sum_1)


# 排序：sorted 排序 默认是升序
new_list = sorted(random_list)
print(new_list)
# 排序：sorted 排序 reverse=True
new_list = sorted(random_list,reverse=True)
print(new_list)
























