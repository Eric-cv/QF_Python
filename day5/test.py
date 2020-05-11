'''
break continue 跳转语句

'''
# 方式一
sum = 0
for i  in range(10):
	if i%3 != 0:
		sum += i
print('sum---111',sum)
# 方式二
sum = 0
for i in range(10):
	if i%3 == 0:
		# pass 占位符 
		# break 跳出循环
		continue # 跳过循环体中continue下方的语句不执行，直接执行下一次循环
	sum += i
print('sum---222',sum)
