'''
# 字符串：

'''
# 直接赋值
s1 = 'abc'
s2 = "abc"
s3='''
abc
'''
'''
print(id(s1),id(s2),id(s3)) #三引号占用的内存空间与单双引号的不同（前提三引号的内容不在一行上）

print(s1 == s2) # True  '='  比较的内容
print(s1 is s2) # True  'is' 比较的是地址

print(s2 == s3) # False 
print(s2 is s3) # False 

# input赋值
#s1 = input('请输入：') # 'abc'
#s2 = input('请输入：') # 'abc'

print(s1 == s2) # True 
print(s1 is s2) # Flase （常量赋值的is是True，input底层做了处理所以最后的地址是不一样的）


# 字符串的运算符： + *
s3 =s1 +s2 # +相当于拼接符


s4 = s1 * 5 # 倍数
print(s3)
print(s4)

# in 在...里面
name = 'steven'

result = 'st' in name # 返回值是布尔类型 True False
result = 'ste' in name # True 
result = 'eve' in name # True 
result = 'tv' in name # False 不连着的字母不可以

# not in 不在..里面
result = 'tv' not in name # True
print(result)

# % 字符串的格式化

print('%s说：%s' %(name,'大家好好学习！'))

# r保留原格式 有r 则不发生转义没有r发生转义（例如：\'）
print(r'%s说：\'哈哈哈\'') # 加r没有转义，否则会转义


# [] [:]
filename = 'picture.png'

# 位置都是从0开始，位置我们也会称作下标或者索引
print(filename[1]) # 通过[]可以结合位置 获取字母 特点：只能获取一个字母

# range(1,10)   -----> [1:10] 同样包前不包后
print(filename[0:7]) # 包前不包后

print(filename[3:7]) # 截取字符串

# 省略
print(filename[3:]) # 只要省略的是后面的，表示一直取到字符串的末尾
print(filename[:7]) # 只要省略的是前面的，表示从0开始取值

#负数
print(filename[8:-1]) # -1代表倒数第一个数，取不到哦
print(filename[:-2])  # -2代表导数第二个数，取不到哦
print(filename[-1:])  # 就只取最后一个值，包前不包后，还是把它自己包括了

print(filename[10:0])

# [::]
print(filename[::-1]) 

print(filename[10:0])
'''
# [::-1] 倒序
# str1 = 'abcdefg'
'''
str1 = 'abcdefg'
print(str1[-1:-5:-1]) #倒序输出最后一位到倒数第四位
print(str1[5:0:-1])
print(str1[:])
print(str1[::-1]) #倒序输出所有
'''
'''
str[start:end:方向和步长]
方向：1 表示从左向右 0 1 2 3 4 5
     -1 表示从右向左 5 4 3 2 1 0
     注意数值的顺序
     比如： 正向：5:0 就不行
            反向：5:0 就可以
'''
# 练习：hello world
# 逆序输出 hello world
# 正向输出hello
# 逆序输出整个Hello world
# 打印获取oll
# 打印llo wo
str = 'hello world'
print(str[-1:-6:-1])
print(str[0:5])
print(str[::-1])
print(str[4:1:-1])
print(str[2:-3]) # str[2:8]

#
print(s1[::2]) # 2表示步长，同时也是正序
print(s1[::-2]) # 2表示步长，同时也是倒序


# 字符串的内建函数：声明一个字符串，默认可以调用内建函数（系统准备好的一些函数）
# 第一部分：大小写相关的
#capitalize() title() upper() lower()

message = 'zhaorui is a beautiful girl!'
msg = message.capitalize() #将字符串的第一个字符串转化为大写
print(msg)

msg = message.title() #每个单词的首字符都大写
print(msg)

msg = message.upper() #将字符串的全部转化为大写
print(msg)

msg = message.lower() #将字符串全部转化为小写
print(msg)

# 案例：验证码案例

s='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
print(len(s)) # 求字符串长度，返回值整型
import random

# randint(a,b)  # a和bd都能取到，包左也包右
for i in range(4):

	ran = random.randint(0,len(s)-1)
	code += s[ran]

print('验证码：'+code)

# 提示用户输入验证码
user_input = input('请输入验证码：')
if user_input.lower() == code.lower():
	print('验证码输入正确！')
else:
	print('验证码错误！')


