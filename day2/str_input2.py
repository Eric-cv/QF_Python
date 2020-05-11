'''
游戏：英雄联盟
输入角色：xxx
输入拥有的装备：xxx
输入想购买装备：xxx
输入付款金额：xxx

xxxx 拥有xxx装备，花了xxx钱

知识点：input  格式化输出print()

'''

print('''
*********************
       英雄联盟
*********************
	''')

role = input('输入角色：')
outfit = input('请输入拥有的装备：')
update_outfit = input('请输入想购买的装备：')
payment = input('输入付款金额：')

outfit = update_outfit

print('{}拥有了{}装备，您购买此装备花了{}钱'.format(role,update_outfit,payment))
