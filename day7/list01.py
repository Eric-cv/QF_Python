# 列表的函数：
'''
字符串函数：# 字符串.调用的函数
print('a b c'.split(' ')  ) 
['a', 'b', 'c'].split(' ')  #错误

列表函数：只有通过列表才可以调出来的函数

添加：append extend insert
删除： del list[index]
	  remove(e)  删除列表中第一次出现的元素e，返回值是None，
	             如果没有找到要删除的元素，报异常
	  pop()：弹栈  移除列表中的最后一个元素,返回值是删除的元素
	  			   默认是删除最后一个，但是也可以指定下标删除
	  clear()：清楚列表里面全部元素

翻转：reverse()

排序：sort()
游戏：

'''

hotpot_list = ['海底捞','呷哺呷哺','张亮麻辣烫','热辣一号','宽板凳']

hotpot_list.append('张亮麻辣烫')

print(hotpot_list)

#result = hotpot_list.remove('张亮麻辣烫') #移除列表中某一个值的第一个匹配项
#result = hotpot_list.remove('杨国福麻辣烫')

#print(result)  # None ; remove没有返回值

#print(hotpot_list)


result = hotpot_list.pop() #返回值是删除的元素
print(result)
print(hotpot_list)

result = hotpot_list.pop(2)
print(hotpot_list)


hotpot_list.reverse()  # 改变了列表的位置结构
print(hotpot_list)

hotpot_list[::-1]  # 只是逆序拿出列表中的元素，打印出来
print(hotpot_list)


# 系统提供的排序
'''
sorted(list，reverse = True) # 默认升序
list.sort()

次数：
count()
'''

l = [4, 8, 1, 9, 5, 7 # l.sort()  # 默认升序
l.sort(reverse=True)  #降序 
print(l)


print(l.count(8)) # 查看列表中有几个8







