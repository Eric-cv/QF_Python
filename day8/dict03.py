'''
增加元素(key:value)
dict[key]=value ------>{key:value}

特点：key在字典中是唯一的,value可以不唯一
{'name':'tom','name':'aaa'} 错误定义
{'张三':100, '李四':100, '王五':100} 正确

增加元素对比：
list1=[]
list1.append(element)

dict1 = {}
dict1[key]=value

修改元素：
list1[index]=newvalue
dicta[key]=nwevalue

查询元素：
list[index] -----> elemebt
dict[key] ----> value

取值：字典都是根据key获取value值
'''
list1 = [3, 5, 7, 8]

print(list1[2])  # 列表中找元素根据下标

dict1 = {'1':'张三', '2':'李四', '3':'王五'}
print(dict1['2']) # 字典中找元素根据key

dict2= {'张三'：100, '李四'：100,'王五'：100, '赵柳'：199 }

print(dict2['王五'])  # key

# 考试分数大于90分的人是谁
# 尝试对字典进行遍历

for i in dict2:
	print(i)

# 单独遍历字典的结果就是：字典的key

# 字典里面的函数：
# items()  values() keys()
# items:将字典转成列表保存的形式，键值对以元组的形式保存 [(key,value),(key,value),....(key,value)]
 print(dict2.items()) # items()函数把字典转换成列表中套元组的形式

 for i in dict2.items():
 	print(i)  #('张三',100)

# a, b = ('aa', 'bb') # 用两个值去接元组，则分别赋值
 for key, value in dict2.items():
 	print(key, value)
 	if value>90:
 		print(key)

# value: 取出字典中所有的值
result = dict2.values()
print(result)

# 求所有学生考试成绩平均分
for score in dict2.values():
	print(score)

scores = dict2.values()

totle = sum(dict2.values())
avg = totle/len(scores)
print(avg)

# keys():获取字典中的所有的key键 

names = dict2.keys()
print(names)

for name in names:
	print(name)


# 找人：in  也可以用于字典操作  用于判断元素有没有在字典的key中出现
print('王五' in dict2)

'''
1.可以根据key获取值，如果key在字典中不存在则报出keyerror
	dict[key] = values
2.字典的内置函数：get(key)  ----> value 如果取不到值则不会报错，则返回None
				get(key,default) ---->value 如果能够取到值则返回字典中的值，取不到则返回default的值
				items()
				

'''

#print(dict2['赵飞'])
print(dict2.get('赵飞')) 





































