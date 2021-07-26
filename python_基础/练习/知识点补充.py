# def my_def():
#     print(123)
# print(__name__)
#
#
# # 如果__name__ == main 就执行
# # __name__作为主运行程序 他的值是mian
# # 作为倒入程序时他的值是模块名.方法名
#
# if __name__ =="__main__":
#     my_def()
# 列表生成器
# a = [x for x in range(100)]
# print(a)
# a = [x for x in range(100) if x%2!=0 and x%3==0]
# if type(a) == list:
#     print(123)
# 三元运算
# c = 1 if 5 >6 else 0
# print(c)
# class plane:
#     def __init__(self):
#         self._alives =True
#     def dic_action(self):
#         print("取消事件调度")
#     @property
#     def alive(self):
#         if not self._alives:
#             self.dic_action()
#             print(123)
#         return self._alives
#     @alive.setter
#     def alive(self,value):
#         self._alives = value
#         if value ==False:
#             self.die_alive(value)
#
#
#     def die_alive(self,value):
#         if value == False:
#             print("飞机被撞了了")
#
#
# p = plane()
# p._alives ==False
# p.alive
# class add():
#     def __init__(self,a,b):
#         self.a =a
#         self.b = b
#     @property
#     def add_data(self):
#         return self.a * self.b
# a = add(5,10)
# print(a.add_data)
class add:
    def __init__(self,so):
        self._so = so
    @property
    def sour(self):
        return self._so
    @sour.setter
    def sour(self,valur):

        if not isinstance(valur,int):
            raise print("请输入合法成绩")
        if valur<0 or valur>100:
            raise print("请输入正确成绩")
        self._so =valur


p = add(100)
p.sour = 101
print(p.sour)