# coding=utf-8
# @Time     :2020/4/22 0022 9:31
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :file02.py
# @Software :PyCharm

# 写文件
'''
stream = open(r'..\day11\aaa.txt', 'w')
mode = 'w'  表示就是写操作

方法
    write(内容)  每次都会将原来的内容清空，然后写当前的内容
    writelines(Iterable) 没有换行效果
    stream.writelines(['赌神高进\n', '赌侠小刀\n', '赌圣周星星\n'])
    # 换行自己加

如果mode='a' (append:追加),不清空之前的内容，末尾追加内容

'''
# stream = open(r'..\day11\aaa.txt', 'w')

# 不清空之前的内容，末尾追加内容
stream = open(r'..\day11\aaa.txt', 'a')
s = '''
你好！ 
    欢迎来到澳门博彩赌场，赠送给你一个金币！
            赌王：高进
            
'''
result = stream.write('hello')
print(result)
stream.write('龙五')
stream.writelines(['赌神高进\n', '赌侠小刀\n', '赌圣周星星\n'])
stream.close()  # 释放资源
#stream.write('龙五2号')  # ValueError: I/O operation on closed file.