# 不重复特点
list1 = [3,5,8, 9,1,8,4,2,5,8,9]

# 声明集合：set
s1 = set() # 创建空集合只能使用set()
s2 = {1,3,7} # 字典: {key:value,.... key:value}
		# 集合：{元素1， 元素2, 元素3}

print(type(s2))
print(type(s2))

# 应用：如何将一个列表快速去重 set()
s3 = set(list1)
print(s3)  #{1,2,3,4,5...}

# 集合里面的增删改查：
# 1.增加  s1 = set()
s1.add('hello')

s1.add('小猪佩奇')

s1.add('lucy')

print(s1)

# add() 添加一个元素
# update() 可以添加多个元素， 
t1 = ('林志玲',' 言承旭') 
s1 = update(t1) # {'hello','林志玲'，。。。。}

s1.add(t1)
print(s1)

# 删除 remove 如果元素存在则删除，不存在则报错keyerror 
#      pop  随机删除（一般删除第一个） 
#      clear

s1.remove('言承旭')
print(s1)

s1.pop()
print(s1)

s1.clear() #清空

print(s1)

# discard() 类似remove()  在移除不存在的元素时不会报错





