# from test2 import *
# print("我是test1")
# print(b)
# import test2  1 首先执行test2中的代码
#               2 将b添加到sys.models中
#             3 当前模块创建b变量来指向模块b
# 冒泡排序
a = [1,3,2,1,4,5,6,7,8,0,8,6,54,6,8,76,54,3]
# for i in range(len(a)-1):
#     for b in range(len(a)-i-1):
#         if a[b] < a[b+1]:
#             a[b],a[b+1] = a[b+1],a[b]
# print(a)
# a.sort(reverse=True)
# print(a)
# a = set(a)
# print(list(a))
# b =[]
# for i in a:
#     if not i in b:
#         b.append(i)
# print(b)
# for i in a:
#     data = a.count(i)
#     print(data)
#     if data ==1:
#         pass
#     else:
#         for b in range(0,data-1):
#             a.remove(i)
# print(a)
# 字典排序
# dic_a = {"name":"zhangsan","age":15,"name1":"zhangsan","age1":118,"name2":"zhangsan","age2":30,"name3":"zhangsan","age3":50,}
# sorted(dic_a.values())
# print(dic_a)
sta_a = "      1$3$2$1$2$3$9$4$9$1$8$2$7$3$4$8$7$1$2$0$3$8$4$7$1$0$2$3$7$4$1$7$2$3$8$9$4"
# sta_a="$".join(sta_a)
sta_a = sta_a.split("$")
print(sta_a)