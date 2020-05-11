# 输入：input()

#name = input()

#print(name)


#name = input('请输入你的名字：') #阻塞式

#print(name)


'''
练习：
游戏：捕鱼达人

输入参与游戏者用户名
输入密码：

充值： 500

'''

print('''
*********************
       捕鱼达人
*********************
	''')
username = input('请输入参与游戏者的用户名:\n')
password = input('输入密码：\n')

print('%s请充值才能进入游戏\n' %username)

coins = input('请充值:\n')  # input键盘输入的都是字符串类型
print(type(coins))
coins = int(coins)
print('%s充值成功！当前游戏币是：%d'%(username, coins))
