# def add(x,y):
#     def easy_add():
#         return x+y
#     return easy_add
# a =add(1,6)
# print(a())
# class add:
#     def __passs(self):
#         print(123)



# def is_login(fun):
#     def login(user_name):
#         if user_name =='123':
#             fun()
#         else:
#             print("请登录")
#     return login
# @is_login
# def home():
#     print("欢迎进入首页")
# a = home("123")
# class login:
#     name = False
#     def is_login(self,fun):
#         def warrp(*args,**kwargs):
#             if self.name ==True:
#                 fun(*args,**kwargs)
#             else:
#                 print("请登录")
#         return warrp
# a = login()
# @a.is_login
# def home():
#     print(123)
#
# home()
# 装饰器传递参数
from functools import  wraps
user_login = {'type':False}
def login_requert(size = "foou"):
    def outter_wapper(fun):
        # 添加wraos装饰以可以但会真实函数的name
        @wraps(fun)
        def wapper(*args,**kwargs):
            if user_login["type"] == True:
                fun(*args,**kwargs)
            else:
                if size == "foou":
                    print("跳转到前台")
                else:
                    print("跳转到后台")
        return wapper
    return outter_wapper

@login_requert("foo")
def home():
    print("欢迎进入首页")

home()
print(home.__name__)

