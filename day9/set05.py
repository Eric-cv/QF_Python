# 类型转换
# str() int() list() tuple() set() dict()

# str() ---> int,list,set,tuple
s = '8'
i = int(s)

s = 'abc'
l = list(s)
print(l)  # ['a', 'b', 'c']
s = set(s)  # {'a', 'b', 'c'}
print(s)

t = tuple(s) # ('a', 'b', 'c')
print(t)

# 反过来： str() <--- int,list,set,tuple,dict,float
i = 8
s = str(i)

l = str(['a','b','c'])
print(l)  # '['a,'b','c']'

# list--> set() tuple(), 可以转成字典[(key,value),(key,value)...]
# tuple--> list set-->list
tuple1 = (1,2,3,4)
print(list(tuple))

set1 = {1,2,3,4}
print(list(set1))

dict1 = {1:'a', 2:'b'}
print(list(dict1))  # 只是将key放入了list

