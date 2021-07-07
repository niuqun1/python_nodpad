# 什么是列表：列表相当于一个容器他可以存储不同的数据类型÷
# 定义一个列表
list_data = ['name','age','sex',123]
list_data1 = ['name','age','sex',123]

# print(list_data)
# # 列表追加元素,可以追加列表
# list_data.append('time')
# print(list_data)
# list_data.append(['123'])
# print(list_data)
# # 列表循环
# for i in list_data:
#     print(i)
# # 列表下标,与字符串的下标操作一致
# print(list_data[1])
# print(list_data[::-1])
# # count 统计列表某个元素出现的次数
# print(list_data.count(123))
# # except将另一个列表追加到另一个列表的后面
# list_data.extend(list_data1)
# print(list_data)
# Index在列表查找某个元素的下标，若列表不存在抛出异常,列表不支持find方法
# print(list_data.find(123))
print(list_data.index(123))
# insert方法将元素插入指定位置
list_data.insert(0,'我是插入的数据')
print(list_data)
# pop删除列表中的元素,根据下标删除，不填写元素默认删除最后一个
list_data.pop(0)
print(list_data)
# remove删除列表中的元素默认删除第一个匹配的
list_data.remove('name')
print(list_data)
# reverse列表反转
list_data.reverse()
print(list_data)
# sort将列表排序会更改列表的植
list_num = [1,2,6,5,34,23,679,67,4,23,5,7,54,3,2,4,5,7]
print(id(list_num))
# list_num.sort()
print(id(list_num.sort()))
print(list_num)
del list_num[2]
print(list_num)