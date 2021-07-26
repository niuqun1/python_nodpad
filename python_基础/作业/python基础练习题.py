# a = 1
# b = 2
# print(a == b)
# print(a!=b)
# print(a >= b)
# print(a <= b)
# num = input("请输入")
# c={"lily":19,"lucy":18,"rose":25,"daizy":16} 
# data = sorted(c.items(),key = lambda kv: kv[1])

# print(data)

# s = "aedffiibllbbbe"
# data = set(s)
# data1 = list(data)
# data1.sort(reverse = True)
# data =''.join(data1)
# print(data)
# data = input("请输入内容")
# if len(data) <12:
#     # data.reverse()
#     # data = "".join(data)
#     # print(data)
#     # print(data[::-1])
#     data1 = []
#     for i in range(1,len(data)+1):
#         print(i)
#         b = len(data)-i

#         data1.append(data[b])
#     print(data1)

# else:
#     pass
# data = input()
# data = list(data)
# data.sort()
# print(data)
# a=1

# while a <=9:
#     b=1
#     while b<=a:
#         print(b,a)
#         b+=1
#     a+=1

# def password(a,b):
#     c= 1
#     while c<=3:
#         user = input()
#         password = input()

#         if user == str(a) and password == str(b):
#             print("登陆成功")
#             break
#         else:
#             c+=1

# password(1,2)
# a=1
# c=0
# while a <=100:
#     if a % 2 !=0:
#         c+=a
#     print(c)
#     a+=1
# dict1 = {"1":1,"2":2,"3":[1,2,3,4]}
# dict1["3"] = [1,2,3,4,5,6,7]
# print(dict1)
# dict1["3"].insert(0,"0")
# print(type(dict1["3"]))
# print(dict1)
# s ="132134123sdfasdfasdf"
# print(list(s))
# print(tuple(s))
# data2 = {}
# a = [1,2,3,4,5,6,7,8,9]
# data = a[0:4]
# data1 = a[5:8]
# data2["k1"] = data
# data2["k2"] =data1
# print(data2)
# a ="aaaaaaabbbbbbbbbccccccdddd"
# data_dic = {}
# for i in a:
#     data = a.count(i)
#     data_dic[i] = data
# print(data_dic)
# data = "hello word go"
# print(data.startswith("h"))
# print(data.endswith("o"))
# data = data.replace("go","move")
# print(data)
# a = 100
# b =0
# for i in range(1,2):
#     print(i)
#     a /=2
# print(a)
# a = ['a','b','v','a','c','v']
# a = set(a)
# print(a)

# a = "hello word"
# print(a[::-1])
# a =list(a) 
# a.reverse()
# a ="".join(a)
# print(a)  
# a = [1,2,3,4,5,6,7]
# b = [0,9,8,7,6,6,4,2,5]
# a.extend(b)
# print(a)
# a.sort(reverse=True)
# print(a)
# a = "hello word"
# '/t'.join(a)
# print(a)

# print(a.index(" "))


# a = input()
# if a.find(" ") == -1:
#     print(a,len(a))
# else:
#     print(a[a.find(" ")::],len(a[a.find(" ")::]))
# a = [1,2,3,4,'a',1,'b',4,'c']
# print(a[4::2])
# for  i in range(1,100):
#     print(100 -i)
# a = []
# for i in range(1,101):
#     a.append(i)
# print(a[::3])
# 函数式编程练习：
# 练习filter函数：使用filter函数过滤掉小于3的数：
# from os import name


from os import name


# a = [1,2,3,4,5,6,7,8,1,2,1,2]
# data = filter(lambda x:x>3,a)
# for i in data:
#     print(i)


# 练习map函数：使用map函数将以下数组中所有的数都扩大10倍：

#  a = [1,2,3,4,5,6]
# data = map(lambda x:x*10,a)
# for i in data:
#     print(i)

# 练习reduce函数：使用reduce函数求以下列表中数值之和：

# from functools import reduce
# from functools import reduce
# data = reduce(lambda x,y:x+y,a)
# print(data)

# 实现一个复制图片功能的程序：
# 用户输入图片的地址和名字，以及指定的图片。
# def cp_jpeg(file,cp_file):
#     with open(file,"rb") as fp:
#         with open(cp_file,"wb") as fp1:
#             fp1.write(fp.read())
# cp_jpeg("12.jpeg","cp_12.jpeg")


# 实现一个宠物寄养管理系统，要求如下：
# 1. 需要使用函数来模块化。
# 2. 宠物的信息包括：宠物编号/宠物名称/宠物种类/一天的价格。
# 3. 需要实现：添加/查找/删除/退出程序的功能。
# 4. 要求使用文件来存储信息，下次打开系统，数据依然存在。
# 1 写入函数、
# data_list = [{'id': '3', 'name': '牛群'}]
# def write_Data(data):
#     with open("data.txt","w") as fp:
#         fp.writelines(data)
# write_Data(data_list)
# # # 2增
# def add_data(name,id):
#     data_list=read_data()
#     data_dic = {}
#     data_dic["id"] = id 
#     data_dic["name"] = name
#     data_list.append(data_dic)
#     write_Data(data_list)
#     print("写入成功")
# # 3改
# def updata_data(data,new_Data):
#     for i in data_list:
#         if i["id"] == data:
#             i["name"] = new_Data
#     write_Data(data_list)

# # 4查
# def find_data(data,new_Data):
#     for i in data_list:
#         if i["id"] == data:
#             print(i)
# # 5读取数据
# def read_data():
#     with open("data.txt","r") as fp:
#         data = fp.read()
#     global data_list
#     data_list = data
#     return    data_list
# print(type(read_data()))


# 实现一个密码存储系统：
# 1. 可以存储某个产品的用户名和密码。
# 2. 产品名字和用户名以及密码都必须为英文。
# 3. 提示：可以使用ord函数将英文字符转换为ascii码。
# 用面向对象思想重写宠物寄养管理系统


# data = []
#
# def add_pet():
#     id = input("请输入用户id")
#     name = input("请输入用户名称")
#     user = {}
#     user["id"] = id
#     user["name"] = name
#     data.append(user)
#
#     print("用户添加成功")
#
#
#
# def updata_pet():
#     user_id = input("请输入要修改用户id")
#     user_name= input("请输入要更改的名字")
#
#     for i in data:
#         if i["id"] == user_id:
#             i["name"] == user_name
# def sava_pet():
#     with open("data.txt","w") as fp:
#         links = []
#         for i in data:
#             text = f"{i['id']}/{i['name']}\n"
#             links.append(text)
#         fp.writelines(links)
#
# def find_pet():
#     user_id = input("请输入要查询用户id")
#
#     for i in data:
#         if i["id"] == user_id:
#             print("用户id{},用户名称{}".format(i["id"],i["name"]))
#
# def delect_pet():
#     user_id = input("请输入要删除用户id")
#     for i in data:
#         if i["id"] == user_id:
#             data.remove(i)
# def get_sava_data():
#     with open("data.txt","r")as fp:
#         for i in fp:
#             text = i.split("/")
#             id = text[0]
#             name = text[1]
#             print("用户id{},用户名称{}".format(id,name))
# def get_data():
#     with open("data.txt","r")as fp:
#         for i in fp:
#             text = i.split("/")
#             id = text[0]
#             name = text[1]
#             data.append({"id":id,"name":name})
# get_data()
#
# while True:
#     user_data = input("请输入选择项")
#     if user_data == "1":
#         add_pet()
#         sava_pet()
#
#     elif user_data == "2":
#         updata_pet()
#
#     elif user_data == "3":
#         sava_pet()
#
#     elif user_data == "4":
#         find_pet()
#
#     elif user_data == "5":
#         delect_pet()
#
#     elif user_data == "6":
#         sava_pet()
#         break
#     elif user_data == "7":
#          get_sava_data()
#     else:
#         print("请输入合法数据")
#
#

# 面向对象宠物变成
# class Pet:
#
#     def __init__(self, per_id, pet_name, pet_type, pet_price):
#         self.pet_id = per_id
#         self.pet_name = pet_name
#         self.pet_type = pet_type
#         self.pet_price = pet_price
#
#     def get_pet(self):
#         return f"{self.pet_id}&{self.pet_name}&{self.pet_type}&{self.pet_price}"
#
#     @classmethod
#     def pet_with_link(cls, link):
#         pet_id, pet_name, pet_type, pet_price = link.replace('\n', '').split("&")
#         pet = Pet(pet_id, pet_name, pet_type, pet_price)
#         return pet
#
#
# class Petmanager:
#     __instance = None
#     __filename = "pet_data.txt"
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance = super(Petmanager, cls).__new__(cls, *args, **kwargs)
#             return cls.__instance
#
#     def add_pet(self, per_id, pet_name, pet_type, pet_price):
#         with open(Petmanager.__filename, "w")as fp:
#             p = Pet(per_id, pet_name, pet_type, pet_price)
#             fp.writelines(p.get_pet())
#
#     def read_pet(self):
#         all_pet = []
#         with open(Petmanager.__filename, 'r') as fp:
#             for link in fp:
#                 pet = Pet.pet_with_link(link)
#                 all_pet.append(pet)
#         return all_pet
#
#
# class Applivation:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             Applivation.__instance = super(Applivation, cls).__new__(cls, *args, **kwargs)
#             return cls.__instance
#
#     def __inpet_pet_info(self):
#         pet_id = input("请输入宠物id")
#         pet_name = input("请输入宠物名字")
#         pet_type = input("请输入宠物种类")
#         pet_price = input("请输入宠物价格")
#         pet_maneger.add_pet(pet_id, pet_name, pet_type, pet_price)
#
#     def __print_pet(self):
#         data = pet_maneger.read_pet()
#         for link in data:
#             print("宠物id：{}宠物名字：{}宠物类别{}宠物价格{}".format(link.pet_id, link.pet_name, link.pet_type, link.pet_price))
#
#     def run(self):
#         print("*" * 30)
#         print("0推出系统")
#         print("*" * 30)
#         print("1添加宠物")
#         print("*" * 30)
#         print("2现实所以宠物")
#         print("*" * 30)
#         while True:
#             option = input("请输入操作菜单")
#             if option == "o":
#                 break
#             elif option == "1":
#                 self.__inpet_pet_info()
#             elif option == "2":
#                 self.__print_pet()
#
#
#
# pet_maneger = Petmanager()
# app = Applivation()
# app.run()
# a = f"123456789{data}"
# a.format("abc")
# print(a)
at_command_template = "rosservice call /at{}"
data =""
a = at_command_template.format(data)
print(a)
# print(at_command_template+str(data))


