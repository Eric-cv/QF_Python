# coding=utf-8
# @Time     :2020/5/1 0001 16:01
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :lib_from_outside06.py
# @Software :PyCharm

# 第三方库： pillow  pip install pillow
# import pillow
import requests

response = requests.get('https://www.baidu.com')
print(response.text)

