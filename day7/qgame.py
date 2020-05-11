# 游戏：
'''
1.选择人物
2.购买武器 金币
3.打仗 赢得金币
4.选择删除武器
5.查看武器
6.退出游戏
'''
import random


print('*'*40)
print('\t欢迎来到王者荣耀')
print('*'*40)

role = input('请选择游戏人物：(1.鲁班 2.后裔 3.李白 4.孙尚香 5.貂蝉 6.诸葛亮)')

coins = 1000

# 保存自己的武器
weapon_list = []

print('欢迎{0}来到网者荣耀，当前金币是{1}'.format(role, coins))

while True:
	choice = int(input('请选择：\n 1.购买武器\n 2.打仗\n 3.删除武器\n 4.查看武器\n 5.退出游戏\n'))

	if choice == 1:
		# 购买武器
		print('欢迎进到武器库：')

		weapons = [['屠龙刀',500],['樱花枪',400],['98k',1000],['手榴弹',800],['碧血剑',700],['鹅毛扇',800]]
		for weapon in weapons:
			print(weapon[0],weapon[1],sep='  ')
		# 提示输入要购买的武器
		weapon_name = input('请输入要购买的武器名称：')
		# 1.原来有没有买过武器 2.输入的武器名是否在武器库
		if weapon_name not in weapon_list:
			# 输入的武器名是否在武器库
			for weapon_name in weapons:
				if weapon_name == weapon[0]:
					# 购买武器
					if coins >= weapon[1]:
						coins -= weapon[1]
						weapon_list.append(weapon[0]) # 添加到自己的武器库
						print('{}购买武器:{}成功！'formmat(role,weapon_name))
						break
					else:
						print('金币不足，赶快打仗赚金币')
						break
			else:
				print('输入武器名称错误!')
	else:
			print('已经拥有此武器！')
	elif choice == 2:
		# 打仗 假设你有多个武器
		if len(weapon_list):

			print('进入战场....')
			# 选择武器
			print('{}拥有的武器如下'.formmat(role))
			for weapon in weapon_list:
				print(weapon)

			while True:
				weapon_name = input('请选择：')
				# 
				if weapon_name in weapon_list:
					# 进入战斗 默认跟张飞对战
					ran1 = random.randint(1,20) #张飞
					ran2 = random.randint(1 20)# role

					if ran1 > ran2:
						print('此局对战：张飞胜！')
					elif:
						coins += 200
						print('此局对战：{}胜!，金币：{}'.formmat(role, coins))
				
					else:
						print('此局平局，可以再次对战')
					break
				else:
					print('选择的武器不存在，请重新选择')
		else:
			print('还没有购买武器，赶快去买武器吧！')				
	elif choice == 3:
		# 删除武器
		print('武器太多，很沉，扔几个...')
		if len(weapon_list):
		print('{}拥有的武器如下'.formmat(role))
			for weapon in weapon_list:
				print(weapon)
		
			while True:
				weapon_name = input('请选择要删除的武器名称')
				if weapon_name in weapon_list:
					# 删除武器 remove(obj) pop(index) del(index)
					weapon_list.remove(weapon_name)
					# 思考
					for weapon in weapons:
						if weapon_name == weapon[0]:
							coins += weapon[1]
							break
					break

				else:
					print('武器名输入有误！')
		else:
			print('你都没有武器，还沉什么...，赶快购买去吧！')

	elif choice == 4:
		print('{}拥有的武器如下'.formmat(role))
			for weapon in weapon_list:
				print(weapon)
		print('总金币：',coins)
	elif choice == 5:
		answer = input('确定要离开游戏吗？(yes/no)')
		if answer == 'yes':
			break
	else:
		print('输入错误，请重新选择')
