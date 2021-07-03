# a = "hello"
# b = "word"
# c = a + b
# print(c)
# c = """sdfasdfasdfasdf\
# asdfasdfasd\
# asdfasdf """
# print(c)
# price = 12.84
# # %f 默认展示小数点6位 %f中间添加。x指定展示小数点位数 四舍五入
# data = " iphones is %.1f" % price
# print(data)
# # format的使用
# data = "{},{},{},{}".format(a,b,c,data)
# print(data)
# 字符串下标
# data = "hello word"
# # print(data[1])
# # print(data[-1])
# print(data[0:-1:2])
# print(data[::-1])
# 字符串常见操作


data = "Hello word\t"
# 查看字符串长度
print(len(data))
# 查看字符串类型
print(type(data))
# 查看字符串某字符串下标有多个时返回第一个出现的下标，若字符串没有时报错 
print(data.index('l'))
# print(data.index('a'))

# 查看字符串某字符串下标有多个时返回第一个出现的下标，若字符串没有时返回-1
print(data.find('l'))
# print(data.find('a'))
# replace将字符串里的内容做替换，
print(data.replace('o','O'))
# split将字符串按照某写字段分割返回列表 
data_split = data.split("o")
print(data_split)
# startswith判断字符串是否以xx开头是返回true 不是返回false
print(data.startswith("H"))
print(data.startswith("h"))
# endswith判断字符串是否以xxx结尾
print(data.endswith("rd"))
# 将字符串转换成小写
print(data.lower())
# 将字符串转换成大写
print(data.upper())
# 判断字符串是否全是字母或者数字 是返回true不是返回false
print(data.isalnum())



