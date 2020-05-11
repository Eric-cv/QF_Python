'''
输入两个字符串，从第一个字符串中删除第二个字符串中所有的字符。
例如，输入'They are students.'和'aeiou'
则删除之后的第一个字符串变为'Thy r stdnts.'

'''

s1 = input('请输入第一个字符串：')
s2 = input('请输入第二个字符串：')
s3 = ''
# method1
for i in s1: # 类似于range()
	# print(i,end='')
	if i not in s2:  
		s3+=i

s1=s3
print(s1)

# method2
for i in s2:
	s1 = s1.replace(i,'')
print(s1)

'''
小易喜欢的单词有如下特性：
1.单词每个字母都是大写字母
2.单词没有连续相等的字母
例如：
小易不喜欢"ABBA"，因为这里有两个连续的'B'
小易喜欢"A","ABA"和"ABCBA"这些单词
给你一个单词，你要回答小易是否会喜欢这个单词
'''

word = input('请输入单词：') #HELLO word[0] word[1]
for i in range(len(word)):  # 循环单词长度的次数
	if word[i]<'A' or word[i]>'Z':
		print('不喜欢')
		break
	else:
		# A~Z
		if i < len(word)-1 and word[i]==word[i+1]:
			print('不喜欢！')
			break
else：
	print('喜欢！')


'''
循环提示用户输入：用户名 密码 邮箱（要求用户输入的长度不超过
20和字符，超过则只有前20个有效）
打印输出
用户名 密码 邮箱
admin  123  hfjs@163.com
Lily   111  yweuyr@163.com

如果用户输入q或Q表示不再继续输入
'''
s=''
while True:
	username=input('请输入用户名：')
	password=input('请输入密码：')
	email=input('请输入邮箱')

	username=username[0:20]
	password=password[0:20]
	email=email[0:20]

	msg='{}\t{}\t{}\n'.format(username,password,email)

	msg=msg.expandtabs(20)

	s+=msg

	if username=='q' or username=='Q' or password=='q' or password=='Q' or email=='q' or email=='Q':
		break
print(s)


