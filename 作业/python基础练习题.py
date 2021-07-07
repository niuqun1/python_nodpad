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
a = []
for i in range(1,101):
    a.append(i)
print(a[::4])




