# coding=utf-8
# @Time     :2020/4/24 0024 9:48
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :exception01.py
# @Software :PyCharm

# 语法错误和异常
# 语法错误
# 异常

'''
def divide(a, b):
    return a / b


divide(1, 0)  # ZeroDivisionError: division by zero
'''

# 异常处理：
'''
try:
    pass  # 可能出现异常的代码
except:
    pass  # 如果有异常执行的代码
finally:
    pass  # 无论是否存在异常都会被执行的代码
    
情况1：
 try:
    有可能会产生多种异常
 except 异常的类型1:
    print('')
 except 异常的类型2:
    print('')
 except 异常的类型3:
    print('')
  ....
'''


def func():
    try:
        n1 = int(input('输入第一个数字:'))
        n2 = int(input('输入第二个数字:'))
        per = input('输入运算符号(+ - * /):')

        if per == '+':
            result = n1 + n2
        elif per == '-':
            result = n1 - n2
        elif per == '*':
            result = n1 * n2
        elif per == '/':
            result = n1 / n2
        else:
            print('符号输入有误！')

        print('结果是：', result)

    except ZeroDivisionError:
        print('除数不能为零！！！')
    except ValueError:
        print('必须输入数字！！！')
    except NameError:
        pass
    except Exception:
        pass
func()
print('------------>')