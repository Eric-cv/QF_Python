# coding=utf-8
# @Time     :2020/4/24 0024 10:27
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :exception02.py
# @Software :PyCharm

# 异常处理：
'''
格式：
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
 except Exception:
    pass

如果是多个except，异常类型的顺序需要注意，最大的Exception要放在最后


情况2：获取Exception 的错误原因
 try:
    有可能会产生多种异常
 except 异常的类型1:
    print('')
 except 异常的类型2:
    print('')
 except 异常的类型3:
    print('')
  ....
 except Exception as err:
    print(err) ------> err 的内容就是错误原因
 pop from empty list ------> 从空列表中删除内容

'''


def func():
    global result
    try:
        n1 = int(input('输入第一个数字:'))  # 可能出现ValueError
        n2 = int(input('输入第二个数字:'))
        per = input('输入运算符号(+ - * /):')

        if per == '+':
            result = n1 + n2
        elif per == '-':
            result = n1 - n2
        elif per == '*':
            result = n1 * n2
        elif per == '/':
            result = n1 / n2   # 可能出现ZeroDivisionError
        else:
            print('符号输入有误！')

        print('结果是：', result)

        # 操作列表
        list1 = []
        list1.pop()  # pop from empty list

        # 文件操作
        # with open(r'E:\Files_plus\Project01\QF_Python\day13\result.txt', 'w') as wstream:
        #     wstream.write('本次是运算结果是：{}'.format(result))
        with open(r'E:\Files_plus\Project01\QF_Python\day13\01.txt', 'r') as rstream:
            # 可能出现FileNotFoundError
            print(rstream.read())

    except ZeroDivisionError:
        print('除数不能为零！！！')
    except ValueError:
        print('必须输入数字！！！')
    # except FileNotFoundError:
    #     pass
    # except NameError:
    #     pass
    except Exception as err:
        # 是其他Error的父类，通常放在最后判断，否则会直接进入Exception
        # 此时若仍然想知道到底是什么原因，可以加as err, err表示具体的错误类型
        print('出错啦！', err)  # [Errno 2] No such file or directory: 'E:\\Files_plus\\Project01\\QF_Python\\day13\\01.txt'


func()
print('------------>')
