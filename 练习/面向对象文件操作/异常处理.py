# try:
#     # a = 1
#     # b = 0
#     # c = a / b
#     print(d)
# except (ZeroDivisionError) (NameError) as fp:
#     print("代码执行错误",fp)
# else:
#     print("代码没有错误")
# finally:
#     print("执行完毕，不知道有错误没")
# 不知道具体报错信息时可以使用 exception 代替
# try:
#     # a = 1
#     # b = 0
#     # c = a / b
#     print(d)
# except Exception as fp:
#     print("代码执行错误",fp)
# else:
#     print("代码没有错误")
# finally:
#     print("执行完毕，不知道有错误没")
#
# def geet(data):
#     if type(data) != str:
#         raise ValueError("传递参数错误")
#
# try:
#     geet(123)
# except ValueError as error:
#     print(error.args)
# # 自定义异常
# class ArgumentError(Exception):
#     def __init__(self,*args,**kwargs):
#         super(ArgumentError,self).__init__(*args,**kwargs)
#         # self.args = args
#         print('参数错误')
#
#
# def greet(name,age):
#     if type(name) != str or type(age) != int:
#         raise ArgumentError('参数类型错误')
#     print('my name is:%s，my age is:%s' % (name,age))
# greet(1,1)

# try:
#     greet('zhiliao','18')
#     raise ArgumentError('name必须为str类型')
# except Exception as error:
#     print(error.args)
#

# 自定义异常

# class Areagr(Exception):
#     def __init__(self,*args,**kwargs):
#         names = args + ("参数错误",)
#         super(Areagr, self).__init__(*names,**kwargs)
#         print("1231231312313")
# def geet(a,b):
#     if isinstance(a,str):
#         raise Areagr
# geet("1",2)

# # 自定义异常
# class errors(Exception):
#     def __init__(self,*args,**kwargs):
#         names = args+("cuowu ",)
#         super(errors, self).__init__(*names,**kwargs)
#
# def geer(a,b):
#     if not isinstance(a,int):
#         raise errors
# geer("1",2)

import random
print(random.randint(1,100))
