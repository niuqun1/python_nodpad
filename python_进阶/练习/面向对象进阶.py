import  types


# d = Dome("张三")
# # # setattr 给对象添加属性
# # setattr(d,'age',18)
# # print(d.age)
# # hasattr 判断对象是否有某个属性
# if not hasattr(d,'age'):
#     setattr(d,'age',100)
# print(d.age)

# 给对象添加动态方法
# class Dome:
#     # slots可以限制对象绑定的属性
#
#     __slots__ = ('name','age')
#
#     def __init__(self,name):
#         self.name = name
# def run(self):
#     print(f"{self.name}在奔跑")
# p1 = Dome("p1")
# p2 = Dome("p2")
# p1.run = types.    (run,p2)
# p1.run()
# # 动态删除对象方法
# del p1.run
# p1.run()
# p = Dome(123)
# setattr(p,'age',100)
# setattr(p,'sex',100)







# 对象动态添加方法
class Dome:
    def __init__(self,name):
        self.name = name

# d = Dome("张三")
# setattr(d,'age',100)
# a = getattr(d,'age')
# print(a)
def run(self):
    print(self.name)


d = Dome("张三")
d.run = types.MethodType(run,d)
d.run()




