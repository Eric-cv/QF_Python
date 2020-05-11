# 增删改
brands  = ['hp', 'dell', 'thinkpad','支持华为', 'lenovo', 'mac', '神州']

# 改
print(brands)
print(brands[-1])

brands[-1]='HASEE'  # 赋值  步骤：1.找到 使用下标 2.通过赋值覆盖
print(brands)

# HUAWEI
for brand in brands:
	if '华为' in brand:
		brand = 'HUAWEI'
print(brands)

for i in range(len(brands)):
	# i是0，1，2，3.... ---->下标
	if '华为' in brands[i]:
		brands[i]='HUAWEI'
		break
print(brands)
 
 # 删除 del 

 del brands[2]

 print(brands)


# 删除 只要是 hp mac 都要删除

for i in range(len(brands)):
	# 0 1 2 3 1 4 5 6
	if 'hp' in brands[i] or 'mac' in brands[i]:
		# 超出索引，不能边删边遍历
		del brands[i]
print(brands)

l=len(brands)
i=0
while i<l:
	if 'hp' in brands[i] or 'mac' in brands[i]:
		del brands[i]
		l-=1
	i+=1
print(brands)


'''
word = ['hello','good','apple','world','dight','alpha']
提示输入一个单词比如：hello，如果输入的单词在列表中则删除
最后打印删除后列表
'''

words = ['hello','good','gooo','world','digot','alpha']
w = input('请输入一个单词：')
# 方式1：
# if w in words:
# print('存在此单词')

# '' in ['abc', 'hello', 'aaaa', ....]  # 'abc'有没有在列表里面出现
# 'go' in 'good' 判断字符串'go'有没有出现在字符串'good'中出现，相等或包含
# 'go' == 'go' 判断字符串内容是否相等
# in 的条件判断包含 ==
	#if w in word:  # w in word 判断字符串w有没有在字符串word中出现
		#print('存在此单词！')
		#break

# 方式2（错误）：
for word in words:
	if w in word:
		del word # 这只是把变量删除了，没有删除列表中的word，要用下标删除
		break

# 方式2：
words = ['hello','good','gooo','world','digot','alphago']
w = input('请输入一个单词：')
i = 0 # 表示下标
l = len(words)  # 5
while  i<l:  # i<5
	if w in words[i]:
		del words[i]
		l-=1
		#方法1
		#i-=1
		#方法2
		continue
	i+=1

print(words)
