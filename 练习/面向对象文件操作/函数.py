# # 函数
# # 函数的定义
# def add(a,b):
#     print(a,b)
#     c = a+b
#     return c
# # 关键字参数
# print(add(b=10,a=20))
# # 位置参数
# print(add(10,20))
# # 形参 ：定义函数时的参数
# # 实参 ：调用函数时的参数
# # 位置参数 参数 根据形参顺序给定的
# # 关键字参数 ： a=xx b = xx
# # *args, **kwargs 分别代表却省的位置参数和关键字参数
# # def ptiny_data(*args, **kwargs):
# #     print(args)
# #     print(kwargs)
# #     print(type(args))
# #     print(type(kwargs))
# # ptiny_data(1,2,3,b=10,a=100)
# # a = ('a','b','c')
# # b = {"username":"zhiliao","age":18}
# # *args 获取到的时元祖 **kwargs 获取到的时字典
# ptiny_data(*a,**b)
# # 混合参数 :位置参数必须要在关键字参数前面
# add(10,b=100)
# data_dict = {"name":123}
# def glble_data(data_dict):
#     data_dict["age"]=30
#     print(data_dict)
# glble_data(data_dict)
# print(data_dict)
# global全局遍历
# name = "zhiliao"
# def dome():
#     name = 'zhangsan'
#     print(name)
# def dome1():
#     global name
#     name = "lisi"
#     print(name)
# dome()
# print(name)
# dome1()
# print(name)
# 字典列表元祖 想要修改 变量的指向需要添加global关键
# data_dict = {"name":123}
# data = {"age" :30}
# def glble_data(data):
#     global data_dict
#     data_dict = data
#     print(data_dict)
# glble_data(data)
# print(data_dict)
# persons  = [
#     {"name":'zhangsan',
#      "age":30
#     },
#     {"name":'zhangsan',
#      "age":40
#     },
#     {"name":'zhangsan',
#      "age":20
#     },
# ]
# print(persons)
# def sort_pem(data):
# lis = [{ "name" : "Taobao", "age" : 100},  
# { "name" : "Runoob", "age" : 7 }, 
# { "name" : "Google", "age" : 100 }, 
# { "name" : "Wiki" , "age" : 200 }] 
  
# print(sorted(lis,key=lambda x :x["age"]))
a = [1,2,3,2,1,4,5,6,8,7,65,43,24]
# data = filter(lambda x :x>3 ,a)
# for i in data:
#     print(i)
data1 = map(lambda x :x*10,a)
for i in data1:
    print(i)