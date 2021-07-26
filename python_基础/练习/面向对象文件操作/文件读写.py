# 文件写入？
# fb = open("./data.txt",'w')
# fb.write("hello word")
# fb.close()
# fp  = open("./data.txt",'r')
# data = fp.read()
# print(data)
# fb.close()
# 写入文件
# fp = open("./data.txt",'w')
# fp.write("woshi xieru wenjain ")
# fp.close()
# 读取文件
# fp = open("./data.txt",'r')
# data = fp.read(2)
# print(data)
# fp.close()
# 读取一行
# fp = open("./data.txt",'r')
# # data =fp.readline()
# # print(data)
# # 读取所有内容返回一个列表
# data = fp.readlines()
# data = "".join(data)
# print(data)
# r方法 读取文件 read 不可以操作写入，文件不存在报错
# fp = open('./data.txt','r')
# print(fp.read())
# w方法 写入方法 文件不存在重新创建文件，文件有内容覆盖内容
# a方法 追加方法写入       不可以操作读取
# r+方法 读取方法增加写入方法会覆盖之前内容, 文件不存在报错
# fp = open('data.txt','r+')
# print(fp.write("123"))
# fp.close()

# w+写入方法增加读取方法 无论是读取知识写入都会吧之间文件删除重新创建 所以只能读取空字符串
# fp = open('data1.txt','w+')
# print(fp.write("123"))
# print(fp.read(),123)
# fp.close()
# fp = open('./data.txt','r')
# print(fp)
# for i in fp.readlines():
#     # print(i)
#     print(fp.tell())  
# fp.close()
# with open('data.txt',"r") as fp:
#     fp.seek(0,2)
#     data =fp.tell()
#     data -= 3
#     fp.seek(data,0)
#     data = fp.read()
#     data = list(data)
#     data.reverse()
#     print(data)
# with open("123.jpeg","rb") as fp:
#     with open("456.jpeg","wb") as fp1:
#         fp1.write(fp.readline())
# with open("123.jpeg","rb") as fp:
#     with open("456.jpeg","wb") as fp1:
#         data = fp.read()
#         print(data)
         
#         fp1.write(data)data
# 字典排序
# 
# a =sorted(a.items(),key = lambda x:x[1] )
# print(a)
# 冒泡排序
# a = [9,8,7,6,5,4,3,2,1]
# for i in range(0,len(a)):
#     for b in range(0,len(a)-i-1):
#         if a[b]>a[b+1]:
#             a[b],a[b+1] = a[b+1],a[b]
# print(a)            
# a.sort()
# print(a)
# a = sorted(a,reverse=True)
# print(a)
# a = [{ "name" : "Taobao", "age" : 100},  
# { "name" : "Runoob", "age" : 7 }, 
# { "name" : "Google", "age" : 100 }, 
# { "name" : "Wiki" , "age" : 200 }] 
# a = sorted(a,key= lambda x :x["age"])
# print(a)\


a =[]
with  open("123321.txt","r") as fp:
    b =True
    for i in fp:
        if  i.startswith("<bpde>"):
            b =False
            print(b)
        elif i.startswith("<p>"):
            b =  True

        else:
            if  b:
                a.append(i)
        print(a)
with open("123321.txt","w") as fp1:
    fp1.writelines(a)