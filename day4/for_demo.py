'''
应用场景：
1.猜大小 ---》反复猜大小
2.消消乐 ---》反复充值
3.用户登录 ---》登录多次
  用户名
  密码

循环结构：
for 变量名 in 集合：
	语句

怎么用？

'''
# 使用系统给定range()完成范围指定
#print(range(8))   # range(0,8)  包含0但是不包含8

# 打印三次hello
# for i in range(20): # 三次就写3
# 	print('You must be admitted by UC Berkeley',i)

# print('---game over---')

'''
循环：吃5个馒头
'''
#name = '赵飞'
# 方式1：
# for i in range(5):
# 	#i += 1
# 	print('{}很饿，正在吃第{}个馒头'.format(name,i+1))
#print('{}说：终于吃饱啦！'.format(name))
 
#方式2：
# for i in range(1,6): #1.2.3.4.5 
# 	print('{}很饿，正在吃第{}个馒头'.format(name,i))
# print('{}说：终于吃饱啦！'.format(name))

# range(n)  ---> 0~n-1
# range(m,n) ---> m~n-1

'''
吃馒头：第三个馒头上抹了一点‘鹤顶红’
'''
# name = '张无忌'
# for i in range(1,6):
# 	#判断i的值是多少，i=3别吃
# 	if i==3:
# 		print('{}，赶快扔掉这个馒头，有剧毒：\'鹤顶红\'！！！'.format(name))
# 	else:
# 		print('{}很饿，正在吃第{}馒头'.format(name,i))

'''
for  ... else
else：适用于for执行完或者没有循环数据时，需要做的事情

pass  空语句
只要有缩进而缩进的内容还不确定是时候，此时为了保证语法正确性，就可以使用pass占位，
不会报出语法错误。
'''
# name = '赵飞'
# num = int(input('请输入需要的馒头数量：'))
# for i in range(num):
# 	print('{}很饿，正在吃第{}馒头'.format(name,i))
# else:
# 	print('还没有给我馒头，{}快饿哭啦！'.format(name))

# print('------------')


# if 10 > 7:
# 	print('10是大的')
# else:
# 	pass

# print('---判断结束---')

# 用户的账户密码登陆而且只能登陆三次，如果三次未成功账户锁定
# break 关键字
# for i in range(3):
# 	username = input('请输入用户名：\n')
# 	password = input('请输入密码：\n')
# 	# 验证用户名和密码
# 	if username == 'songsong' and password == '123456':
# 		print('欢迎！用户：{}'.format(username))
# 		print('-----轻松购物吧-----')
# 		break
# 	else:
# 		print('用户名或密码错误')
# else:
# 	print('账户被锁定，需要被重新激活！') # 三次输入错d
# 	误的时候

for i in range(3):
	if i == 4:
		print('这家店是黑店，馒头有毒！等着关门吧！')
		break # 跳出循环结构
		print('abcd') # 即使有语句也不会执行，干脆别写！
	else:
		print('这家的馒头真香啊!要多吃几个呀！')
	else:
		print('--->进入消协会大门')
'''
range的范围正常执行完毕，而没有异常break跳出。就可以执行else，
只要有break旧不会执行else



'''











