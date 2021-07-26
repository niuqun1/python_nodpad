# # 定义字典
# from typing import KeysView


data_dict = {'name':"zhangsan","sex":"男"}
# # 获取字典值÷
# print(data_dict['name'])
# # 修改字典值
# data_dict['name'] = '李四'
# print(data_dict)
# # 获取字典长度
# print(len(data_dict))
# # 遍历字典Keys
# for i in data_dict.keys():
#     print(i)
# # 遍历字典
# for k,v in data_dict.items():
#     print(k,v)
# # 删除字典
# del data_dict['name']
# print(data_dict)
# del data_dict
# print(data_dict)
#  
from functools import update_wrapper


a = {'url':'http://www.baidu.com/','title':"baidu"}
b = {"url":"http://www.google.com/",'new_value':"new_value"}
# 清空字典
# a.clear()
# print(a)
# get方法获取字典值 不存在不会抛异常
# print(a.get('url'))
# print(a.get('name'))
# pop 用来过去给定建的值然后删除他们 若不存在报错
# print(a.pop('url'))
# print(a.pop('x'))
# popitem 移除字典里的值 因为字典是无序的所以会随机移除
# print(a.popitem())
# update 用来更新 2个字典 若果重复会覆盖字典
a.update(b)
print(a)