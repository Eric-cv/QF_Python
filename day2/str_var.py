person = '大圣哥'
address = '北京市海淀区中关村智诚科技大厦4层'
phone = '15858588888'
num = 5
# '+' 加号 拼接 字符串+字符串 ——>OK ， 字符串+int ———>TypeError
# print('订单的收件人是：'+person+'收货地址是'+address+'联系方式：'+phone+'商品数量'+num)
print('订单的收件人是:%s\n收货地址是:%s\n联系方式:%s\n商品数量是：%s' %(person,address,phone,num))

