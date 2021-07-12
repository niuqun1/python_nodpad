# 定义类使用class
# self代表类本身一我
# 受保护的属性使用下划线开头
# class dome:
#     def __init__(self,name,age) :
#         self.name = name
#         self._age = age
#     def dome1(self):
#         print(self.name)
# data = dome(123)
# data.name = "hello word"
# data.dome1()
# 私有属性
# class proson:
#     def __init__(self,age):
#         self.__age == age
#     def doma(self):
#         print(self.__age)
# p = proson(12)
# p.doma()
# class persion:
#     def __init__(self,password):
#         self.__password = password
    
#     def __accare_password(self):
#         print("这是一个私有方法")
#     def get_Data(self,password):
#         if password == self.__password:
#             return self.__accare_password()
#         else:
#             print("密码错误")
# p = persion("111111")
# p.get_Data("111111")
# # 获取私有属性
# # print(p._persion__password)
# # # 获取私有方法
# # print(p._persion__accare_password())


# class CPU(object):

#     def __init__(self,brand,core,ghz,interface):
#         self.brand = brand
#         self.core = core
#         self.ghz = ghz
#         self.interface = interface

#     def run(self):
#         print('{}牌子，核心数为{}跑起来了'.format(self.brand,self.core))

# class RAM(object):

#     def __init__(self,brand,size):
#         self.brand = brand
#         self.size = size

#     def run(self):
#         print('{}牌子，尺寸为{}的内存跑起来了'.format(self.brand,self.size))


# class Disk(object):

#     def __init__(self,brand,size):
#         self.brand = brand
#         self.size = size

#     def run(self):
#         print("{}牌子，大小为{}的硬盘跑起来了".format(self.brand,self.size))

# class Computer(object):

#     def __init__(self,cpu_interface,max_ram,max_disk):
#         self.cpu_interface = cpu_interface
#         self.max_ram = max_ram
#         self.max_disk = max_disk
#         self.cpu = 123
#         self.rams = []
#         self.disks = []

#     def add_cpu(self,cpu):
#         if self.cpu:
#             print('该主板已经有CPU了！')
#             return False
#         if cpu.interface != self.cpu_interface:
#             print('该主板的CPU接口与此CPU接口不一致！')
#             return False

#         # self.cpu = cpu

#     def add_ram(self,ram):
#         if len(self.rams) == self.max_ram:
#             print('该主板能容纳内存条已达到上限，不能再添加！')
#             return

#         self.rams.append(ram)

#     def add_disk(self,disk):
#         if len(self.disks) == self.max_disk:
#             print('该主板能容纳硬盘数量已达上线，不能在添加！')

#     def run(self):
#         print('通电了...')
#         # 1. cpu先跑起来
#         if self.cpu:
#             # self.cpu.run()
#             print(self.cpu)
#         else:
#             print('没有CPU，不能跑起来')
#             return

#         # 2. 内存跑起来
#         if len(self.rams) > 0:
#             for ram in self.rams:
#                 ram.run()
#         else:
#             print('没有内存条，不能跑起来')
#             return

#         # 3. 硬盘爬起来
#         if len(self.disks) == 0:
#             for disk in self.disks:
#                 disk.run()
#         else:
#             print('没有硬盘，电脑不能跑起来')
#             return

#         print('电脑跑起来了，你可以上知了课堂学习Python了！')


# def main():
#     cpu = CPU(brand='intel',ghz=2.7,core=4,interface='11211')
#     ram1 = RAM(brand='金士顿',size=4)
#     ram2 = RAM(brand='金士顿',size=4)
#     disk = Disk(brand='tongchi',size=256)

#     computer = Computer(cpu_interface='11211',max_ram=2,max_disk=2)
#     computer.add_cpu(cpu)
#     computer.add_ram(ram1)
#     computer.add_ram(ram2)
#     computer.add_disk(disk)

#     computer.run()

# if __name__ == '__main__':
#     main()
# 析构函数 内存销毁是执行
# class doem_del:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# class doma(doem_del):
#     def manapy(self):
#         print(self.name)
# p1 = doma(1,2)
# p1.manapy()
# class cpu:
#     def __init__(self,name,size):
#         self.name = name
#         self.size = size
#
#     def run(self):
#         print(f"{self.name}牌cpu{self.size}个核")
# class master:
#     def __init__(self,name,size):
#         self.name = name
#         self.size =size
#
#     def run(self,run):
#         if run.name == self.name and run.size == self.size:
#             print("主机可执行")
# def main():
#     masters =master(name="inte",size="8")
#     cpus =cpu(name="inte",size="8")
#     masters.run(cpus)
# main()
# # 类的继承
# class master_one(master):
#     pass
# p1 = master_one(name="inte",size="8")
# p2 =cpu(name="inte",size="8")
# p1.run(p2)
# 重写父类

# 父类不满足子类需求可以重写父类
# 当父类跟子类拥有同样的方法时，会直接执行子类 需要执行父类时super(类名，self).函数（）
# class person:
#     def __init__(self,name,sex):
#         self.name = name
#         self.sex = sex
#     def eat(self):
#         print("人正在吃饭")
# class studict(person):
#
#     def eat(self):
#         super(studict, self).eat()
#         print("学生正在吃饭111")
#     def geert(self):
#         print(f"{self.name}{self.sex}")
# p1 = studict("张三","男")
# p1.eat()
# p1.geert()
# 子类不能继父类私有方法和变量
# class person:
#     def __init__(self,name):
#         self.name = name
#     def geet(self):
#         print(self.name)
#
# class studict(person):
#     def sat(self):
#         print(self.name)
# stu = studict("zhangsan")
# stu.sat()
# # __class__ 用来查看对象属于那个类
# print(stu.__class__)

# 多继承x
# class cart:
#     def run(self):
#         print("马在奔跑")
# class lv:
#     def run(self):
#         print("lv在拉磨")
# class louzi(cart,lv):
#     def run(self):
#         # 如果要指定父类方法使用类名字调用
#         cart.run(self)
#         print("lv")
#
# p = louzi()
# p.run()
# print(louzi.__mro__)
#
# 类多态
# class proson:
#     def eat(self):
#         print("人在跑步")
# class dog:
#     def eat(self):
#         print("人在走路")
# hero = None
# data = input()
# if data == 1:
#     hero = proson()
# else:
#     hero = dog()
# hero.eat()

# 类属性和实例属性
# 实例属性：绑定到对象的属性是实例属性，只在当前对象中生效
# 类属性 ：对象可以访问类属性，如果通过对象修改类属性，其实是给对象重新创建了一个相同名字的属性

# class prosin:
#     mame = "张三"
#     def __init__(self,name):
#         self.mame =name
#     def eat(self):
#         # 若没有类中没有实例属性name 那么使用self.name跟prosin.name一样
#
#         print(self.mame,prosin.mame)
# p = prosin("李四")
#
# p.eat()
# 类方法与实例方法
# 实例方法不可以使用类调用只能通过对象调用
# class peosion:
#     clor = "张三"
#     def per(self):
#         print(self.clor)
# # 类方法第一个参数必须是cls 代表当前类
# # 对象可以调用类方法 类不可以调用实例方法 类方法不可以调用实例属性
#     @classmethod
#     def class_per(cls):
#         cls.clor = "李四"
#         print(123,"class",cls.clor)
#     @staticmethod
#     def you_staticmethod():
#         print("我是静态方法")
# # peosion.you_staticmethod()
# p1 =peosion()
# p1.you_staticmethod()

# 类可以更改类方法
# peosion.class_per()
# p = peosion()
# p.per()
# peosion.per()
# p1 =peosion()
# p1.per()
# p1.class_per()
# peosion.class_per()
# 静态方法:不需要传递 cls，self 可以使用类调用 也可以使用对象调用。静态函数不可以直接调用类属性 需要类名。属性


# __new__ 要return super().__new__(cls) 否则创建的对象全是none
# class person:
#     def __new__(cls, *args, **kwargs):
#         print("__new_方法执行了")
#         # return super(person,cls).__new__(cls)
#
#     def __init__(self):
#         print("__init__方法执行了")
#     def __del__(self):
#         print("__del__方法执行了")
# p = person()
# print(p)
# 单列
# class persion:
#     __coune = None
#     def __new__(cls, *args, **kwargs):
#         if not cls.__coune:
#             cls.__coune = super(persion,cls).__new__(cls)
#         return cls.__coune
# p1 = persion()
# p2 = persion()
# print(id(p2),id(p1))


# try:
#     a=1
#     b=2
# except Exception:
#     print("出错了")
# else:
#     print("没有出错")
# finally:
#     print("不知道")

# data = [1,2,3,4,5,6,7,8,9,9,8,7,6,6,7,8,9,8,7,6,7,8]
# data_none = []
# for  i in data:
#     data_index = data.count(i)
#     data_none.append([data_index,i])
# data_none.sort(reverse=True)
# print(data_none)
# data = []
# def faction(lis):
#
#     for i in lis:
#         if type(i)==type(lis):
#
#             faction(i)
#         else:
#             print(i)
#             data.append(i)
#     print(data)
#
#
#
# lis = [1, 2, [4, [5, [6,7, [7,[6,[8,[0]]]], 8],9],0],3,9]
# b =  [1, 2, 4, 5, 6, 7, 7, 6, 8, 0, 8, 9, 0, 3, 9]
# faction(lis)

class dome:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def cllss(cls):
        print(123)
    @staticmethod
    def clas():
        print(123)

p = dome(1,2)
p.cllss()
p.clas()
