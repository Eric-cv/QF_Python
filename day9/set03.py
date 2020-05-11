'''
已知两个列表：
l1 = [5,1,2,9,0,3]
l2 = [7,2,5,7,9]

找出两个列表不同的元素
找出两个列表相同的元素

'''
l1 = [5,1,2,9,0,3]
l2 = [7,2,5,7,9]

s1 = set(l1)
s2 = set(l2)

# 对称差集 ^
result = (s1|s2) - (s1&s2)

print(result)

result = s1^s2 # 两个列表中不一样的元素
print(result)


'''
关键字：set
作用：去重
符号：- & | ^
内置函数：
增加：add() update()
删除：remove() pop() dicard()
运算: difference() intersection() union() symmetric_intersection()
'''

# 可变和不可变
# 不可变：对象所指向的内存中的值是不可变的
# 不可变类型: int str floot tuple
num = 10

s1 = 'abc'
print(id(s1))
s2 = 'abcd'
print(id(s2))

t1 = (3,5,6)
print(id(t1))

t2 = (3,5)
print(id(t2))

# 可变的：对象所指向的内存中的值是可以改变的
# 可变类型：字典dict 列表list
list1 = [1,2,3,4,5]
print(list1, id(list1))
list1.pop()
print(list1, id(list1))

dict1 = {1:'aa', 2:'bb'}
print(dict1, id(dict1))
dict1.pop()
print(dict1, id(dict1))

