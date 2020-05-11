# 字符串内建数：encod 编码 decode 解码
# 编码：网络应用（中文一般会涉及编码问题）
msg = '上课啦！认真听课！' #中文的
'''

'''
# gbk 中文 gb2312 简体中文 unicode

result = msg.encode('utf-8')
print(result)

# 解码
m = result.decode('utf-8')
print(m)


# 字符串内建函数startswith() endwith() 返回值都是布尔类型

# startwith()判断是否是以xxx开头，endwith()判断是否以xxx结尾

# 文件上传

filename = '笔记.doc'

filename.endswith('txt') # filename 是否是以txt结尾的
print(result)

filename.endswith('doc') # filename 是否是以txt结尾的
print(result)

s = 'hello'

result = s.startswith('he')
print(result)

# 只能上传图片（jpg,png,bmp,gif）
file = input('请选择文件：')



# 文件上传 只能上传图片(jpg,png,bmp,gif)

# 分析：要上传的文件路径path，通过文件名再判断是否为图片类型
path = input('请选择文件：')
p = path.rfind('\\')

filename = path[p+1：]  # 通过切片截取出来文件名

# 判断是否图片类型？

if filename.endswith('jpg') or filename.endswith('bmp') or filename.endswith('png') or filename.endswith('gif'):
	print('是图片允许上传！')
else:
	print('不是图片格式，只能上传图片！')	


while  True:
	path = input('请选择文件：')
	p = path.rfind('\\')

	filename = path[p+1：]  # 通过切片截取出来文件名

	# 判断是否图片类型？

	if filename.endswith('jpg') or filename.endswith('bmp') or filename.endswith('png') or filename.endswith('gif'):
		print('允许上传！上传成功！')
		break
	else:
		print('不是图片格式，只能上传图片！')
		





