# coding=utf-8
# @Time     :2020/5/1 0001 15:00
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :random03.py
# @Software :PyCharm

# random 模块
import random

ran = random.random()  # 0-1之间的随机小数
print(ran)  # 0.03761610403400284

# randrange 包左不包右
ran = random.randrange(1, 10)  # randrange(start, stop)
print(ran)  # 9

ran = random.randrange(1, 10, 2)  # randrange(start, stop, step)
print(ran)  # 7

ran = random.randint(1, 10)  # 包左包右
print(ran)  # 3

list1 = ['学强', '飞飞', '家伟', '鹏', '阿文']
ran = random.choice(list1)  # 随机选择列表的内容
print(ran)  # 阿文

pai = ['红桃A', '方片K', '梅花8', '黑桃J']
result = random.shuffle(pai)  # 打乱顺序
print(pai)  # ['方片K', '梅花8', '黑桃J', '红桃A']


# 验证码 大小写字母与数字的组合
def func():
    code = ''
    for i in range(4):
        ran1 = str(random.randint(0, 9))
        ran2 = chr(random.randint(65, 90))
        ran3 = chr(random.randint(97, 122))

        r = random.choice([ran1, ran2, ran3])
        code += r

    return code


code = func()
print(code)  # 16gU
