# 赋值运算符

#1. = 
name = 'admin'

# 将'admin'的值赋给'name'

name1 = name 

print(id(name),name)
print(id(name1),name1)

print(name == name1)  # 判断name和name1是地址是否一致

# 扩展后的赋值符号 += -= *= /= ...
 num = 8
 num += 5  # num = num + 5  此时'+'是数学加号
 print(num)

 a = 'abc'
 a += 'ff'  # 等价于：a = a +'ff'  此时'+'是连接符
 print(a)

