name = '赵飞'
print('姓名是：'+ name )

age = 18
# str(int)  ---> (int -> str)  强制类型的转换
print('年龄是：'+ 'age' ) # 'aaa'  int ---> str
print('年龄是：'+ str(age) ) # 'aaa'  int ---> str
print('年龄是:%s' %age)  # %s--> 是str的简写  底层：str(age),强制类型转换

isMarry = False
print('结婚否？回答：%s' % isMarry)  # str(False) ---->'False'

# %d digit 数字
print('年龄是:%d' %age) 

#age = '18岁'  
#print('年龄是:%d' %age) 

age = 18.5 
print('年龄是:%d' %age) # int(18.5)  --->18 取整

year = 2019
print('今年是:%d' % year) 
print('今年是:%2d' % year) 
print('今年是:%02d' % year)

#%f  folat 四舍五入取小数点后f位
salary = 8899.32895
print('我的薪水是%.1f' %salary)  #四舍五入取小数点后一位
print('我的薪水是%.2f' %salary)  #四舍五入取小数点后二位
 
'''
约起来去楼上看电影，下订单：
movie = '大侦探皮卡丘'
ticket = 45.9
count = 35

格式：
电影：xxxx
人数：xxx
单票价：xxx
总票价：xxx  （小数点后保留一位）
'''
print()
# my answer
message_begining = '约起来去楼上看电影，下订单：'
movie = '大侦探皮卡丘'
ticket = 45.9
count = 35
total = ticket * count
print('%s\n 电影：%s\n 人数：%d\n 单票价：%.1f\n 总票价：%.2f' %(message_begining,movie, ticket, count, total))

#写法1
message = '''
电影：%s
人数：%d
单价：%.1f
总票价：%.1f
'''%(movie,count,ticket,total)

print(message)
