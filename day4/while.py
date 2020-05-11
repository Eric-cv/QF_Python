
# for i in range(1,50,5):
# 	print('--->',i)

'''
range的范围正常执行完毕，而没有异常break跳出。就可以执行else，
只要有break旧不会执行else

range(n) ~ range(0,n)
range(m,n) ~ range(start,end)
range(m,n,step) ~ range(start,end,step)

               3,4
for i in range(5):
	print(i)
0,1,2,



for i in range(5):
	pass
else:
	pass

beak 跳出
'''
'''
while:关键字  完成循环

完整结构：
while 条件:
	语句体（块）
else:
	语句体（块）

'''
#打印1-10之间的数字
#for i in range(1,11)
#	print(i)


i = 1
while i<= 10: # 10<=10 True 11<=10 False 结束循环 
	print(i)
	i += 1

print('打印完毕')


# 打印1-30之间的所有3的倍数
#方式1
n=1

while n<=30:
	#进入循环体
	if n%3==0:
		print('--->',n)
	# 改变n
	n+=1

n=3
#方式2
while n<=30:
	print('===>')
	n+=3

# 打印1-30之既是3的倍数又是5的倍数

n=1

while n<=30:
	#进入循环体
	if n%3==0 and n%5==0:
		print('-------->',n)
	# 改变n
	n+=1

'''
使用while循环计算1-20的累加和
1+2+3+4+...+20
'''
sum = 0
i = 1
while i<=20:
	sum += i
	i+=1

print('累加和是：',sum)

'''
打印三角形
*      --->第1层1颗*
**     --->第2层2颗*
***    --->第3层3颗*
****
*****
# 几层就打几颗
嵌套循环
'''
'''
分析：
1.层数明确
2.发现规律  层数与个数
3.用什么表示层，用什么表示*的个数
'''

ceng = 1
while ceng <= 5: #打5层
	# 打印*
	#print('*'*ceng) #python独有
	#嵌套while循环
	count=1
	while count<=ceng: #每层打和层数一样个数的*
		print('*',end='')
		count+=1
	
	ceng += 1
	print()# 层换行



'''
打印9*9乘法表
1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
...
1*9=9 2*9=18 3*9=27

'''
ceng = 1
while  ceng<=9:
	count = 1
	while count<=ceng:

		print('{}*{}={}  '.format(count,ceng,(count*ceng)),end='')
		count+=1
	ceng+=1
	print()


'''
掷骰子

1.欢迎进入xxxx游戏
2.输入用户名，默认用户是没有币
3.提示用户充值买币（100块钱30币，充值必须是100的倍数，充值不成功提示在此充值）
4.玩一局扣除两个币，猜大小（系统用随机数模拟骰子产生值）
5.只要猜对了奖励1个币，可以继续玩（想不想继续玩，也可以没有金币自动退出）
'''



