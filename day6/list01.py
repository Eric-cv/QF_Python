# 声明
names = ['jack', 'tom', 'lucy', 'superman', 'ironman'] # 列表
computer_brands = []
# 增删改查
# 地址
print(id(names),id(computer_brands))

# 查
# 元素获取使用：下标 索引
#print(names[0]+'\n',names[1],sep='')
#获取列表第一个元素
print(names[0])
print(names[-5])
# 获取列表最后一个元素
print(names[-1])
print(names[len(names)-1])

#结合循环,查询names里面有没有超人
for name in names:
	if name == 'superman':
	print('有超人在里面！')
	break
else:
	print('没有找到超人在里面！')

# 简便
if 'superman' in names: #判断有没有
	print('有超人在里面！')
else:
	print('没有找到超人在里面！')









