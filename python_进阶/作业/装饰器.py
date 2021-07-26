# class Flask:
#     def __init__(self):
#         self.url_view_map = {}
#
#     def route(self,url):
#         def out_wapper(fun):
#             self.url_view_map[url] = fun.__name__
#             def wapper(*args,**kwargs):
#                 fun(*args,**kwargs)
#             return wapper
#         return out_wapper
#
#     def run(self):
#         while True:
#             url = input("请输入要访问的网址")
#             view_fun = self.url_view_map.get(url)
#             if view_fun:
#                 exec(view_fun+"()")
#             else:
#                 print("您访问的页面不存在")
# app = Flask()
# @app.route('/')
# def index():
#     print("欢迎进入index页面")
# if __name__ == "__main__":
#     app.run()
# class Flask:
#
#     def __init__(self):
#         self.view_url =  {}
#
#     def route(self,url):
#         def out_warpppy(fun):
#             self.view_url[url] = fun.__name__
#             print(self.view_url)
#             def warppy(*args,**kwargs):
#                 fun(*args,**kwargs)
#             return warppy
#         return out_warpppy
#
#     def run(self):
#         url = input("请输入你要访问的夜面")
#         view_fun = self.view_url.get(url)
#         if view_fun:
#             exec(view_fun+"()")
#         else:
#             print("访问的页面不存在")
#
# app = Flask()
#
# @app.route('//')
# def index():
#     print("欢迎进入index页面")
#
# if __name__ == "__main__":
#     app.run()

import  time
from  functools import wraps
def out_warppy(fun):
    @wraps(fun)
    def warppy():
        star = time.time()
        fun()
        end = time.time()
        data = end-star
        return data
    return warppy

@out_warppy
def add():
    for i in range(1,10000000):
        pass
print(add(),add.__name__)