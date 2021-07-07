# 定义元祖
from typing import Counter


a = 1,2,3,4,5,5
print(a)
print(type(a))
lise_data = [1,2,1,2,3,43,3,2,12,1,2,3,1]
data_tuple = tuple(lise_data)
print(data_tuple)
data_set = set(data_tuple)
print(data_set)
print(type(data_set))
# 列表与元祖的区别 列表是可变类型 比如长度，元素可以改变 元祖不可以改变，列表是动态数组，元祖是静态 数组÷
# 元祖在字典中可以当做key来使用，列表不可以
# Count 的使用
print(data_tuple.count(1))
aTuple = ('zhiliao',18,'长沙')
username,age,_ = aTuple
print(username)