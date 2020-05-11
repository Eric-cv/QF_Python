# 增加 改 查 (key) 删除
# 删除：
list1=[3,7,9,0]

del list1[1]
print(list1)

dict2= {'张三'：100, '李四'：100,'王五'：100, '赵柳'：199 }

del dict2['王五']
print(dict2)

del dict2['haha'] # keyError

# 字典的内置函数：删除
# dict1.remove('李四')  不存在 报错的
# pop(key[,default])  --->根据key删除字典中的键值对，只有删除成功，返回值是键值对的值
#						pop的默认值，往往是在删除的时候没有找到对应的key,则返回的是默认值

print(result)
result = dict1.pop('张小三'，'字典中没有此键')
print('====>', result)
print(dict1)

# popitem():随机删除字典中的键值对（一般是末尾删除元素）

dict2= {'张三'：100, '李四'：100,'王五'：100, '赵柳'：199 }

result = dict2.popitem()
print(result)
print(dict2)


# clear() 同列表的clear()
dict1.clear()
print(dict1)

'''
删除：
del dict[key]
dict.pop[key]
dict.popitem()
dict.clear()
'''

'''
其他的内置函数:
update()  []+[] 合并操作
fromkeys(seq) ------>将seq转成字典的形式，如果没有制定默认value则用none代替
'''
dict1={0:'tom', 1:'jack',2:'lucy'}
dict2={0:'lily',4:'ruby'}


result = dict1.update(dict2)
print(result)

list1 = ['aa','bb','cc']
new_dict = dict.fromkeys(list1, 10)
print(new_dict)
























