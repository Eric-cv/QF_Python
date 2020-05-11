# 查找相关的，替换

# find() rfind() lfind() index() rindex() lindex() replace()

s1 = 'index lucy lucky goods'

result = 'x' in s1
print(result)

position = s1.find('R') # 返回值是-1则代表没有找到
print(position)
position = s1.find('l') # 如果可以找到则返回字母第一次出现的位置
print(position)
# find('要查找的字符',start,end)
position = s1.find('l',position+1,len(s1)-5) # 也可以指定开始位置查找
print(position)

# https://www.baidu.com/img/bd_logo1.png
url = 'https://www.baidu.com/img/bd_logo1.png'
p = url.rfind('/')  # 从右侧开始检索'/'的位置
print(p)
filename = url[p+1:]
print(filename)

p = url.rfind('.')  # 从右侧开始检索'/'的位置
extention_filename = url[p+1:]
print(extention_filename)

# 替换replace
s1 = 'index lucy lucky goods'
#replace(old,new)
s2 = s1.replace(' ','#') 
print(s2)

s2 = s1.replace(' ','')
print(s2)
