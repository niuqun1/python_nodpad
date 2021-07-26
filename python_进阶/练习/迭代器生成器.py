# 判断一个对象是否是可迭代对象
# from collections import Iterable,Iterator
# print(isinstance([1,2,3,4],Iterable
# select * from data where name between 18 and 20
# a = [1,2,3,4,5,6,7,8,9,8,7,1,2,3,4,5,3,2]
# for i in range(len(a)-1):
#     for b in range(len(a)-1):
#         if a[i]+a[b] ==5:
#             print(a[i],a[b])
# data = filter(lambda x:x>5,a)
# for i in data:
#     print(i)
#     a.remove(i)
# print(a)

# 一个对象如果实现了一个iter方法他就是可迭代对象判断一个对象是否是可迭代对象iterable
# class pet:
#     def __iter__(self):
#         pass
# pes = pet()
# print(isinstance(pet(),Iterable))
# 一个方法如果实现了__next__和__iter__方法那么他就是迭代器对象,判断对象是否是迭代器对象使用Iterator
# class pet:
#     def __next__(self):
#         pass
#
#     def __iter__(self):
#         pass
# print(isinstance(pet(),Iterator))
# class It:
#
#     def __init__(self,star,end):
#         self.star = star
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.star <self.end:
#             tem = self.star
#             self.star+=1
#             return tem
#         else:
#             raise StopIteration()
#
#
#
#
# a = It(1,3)
# for i in a:
#     print(i)

# 迭代器
# class Ite:
#     def __init__(self,star,end):
#         self.star = star
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.star < self.end:
#             self.star+=1
#             return self.star
#         else:
#             raise StopIteration
#
# # 可迭代器对象
# class pet:
#
#     def __init__(self, star, end):
#         self.star = star
#         self.end = end
#
#     def __iter__(self):
#         return Ite(self.star,self.end)
# data = Ite(1,10)#迭代器对象
# print(dir(pet))#可迭代对象
# print(dir(Ite))#迭代器
# print(dir(data))
# # 什么是可迭代对象
# 用来做什么：用来for in 遍历的
# 已知的迭代器类型有哪些 list set tuble dict str
# 需要满足什么条件有 iter  同时需要返回一个迭代器对象
# 迭代器
class iter_data:
    def __init__(self, star, end):
        self.star = star
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.star < self.end:
            self.star += 1
            return self.star
        raise StopIteration


# 可迭代对象
class iter_obj:
    def __init__(self, star, end):
        self.star = star
        self.end = end

    def __iter__(self):
        # 迭代器对象
        return iter_data(self.star, self.end)


# 用来做什么 ： 每次调用next防范返回一个数据
# 需要满足什么条件 需要有 iter 和next方法


# iter函数 用来获取迭代器对象


# 普通列表
# a = [x for x in range(1,100000)]
# print(a)
# 生成器
# 生成器的作用：生成器不会一次吧所有数据加载到内存中，而是调用一次生成一个数据
# a = (i for i in range(1000000))
# for i in a :
#     print(type(i))

# def add(star,end):
#     if star < end:
#        star += 1
#        yield star
# a = add(1,100)
# a = add(1,100)
# a = add(1,100)
# def add():
#     yield 1
#     yield 2
# a =add()
#
# print(next(a))
# print(next(a))
# print(next(a))
# for i in range(1,100):
#     for o in a:
#         print(o)

def add(star, end):
    while star < end:
        temp = yield star
        print(temp)
        star += 1


#
# res = add(1,100)
# print(res)
# print(next(res))
# 定义一个生成器
# a = (i for i in range(1,100))
# 如果一个函数里有yeild那么他就是一个生成器
# 生成器也是迭代器的一种 因为他继承的迭代器，同时也是可叠戴对象 可以通过for 来遍历
# 生成器send方法:在遍历生成器第一个使用send是需要传入none
# a = add(1,10)
# print(a.send(None))
# print(next(a))
# print(next(a))
# print(a.send("hellor"))
# 生成器中如果遇到了return 会抛出异常StopIteration
# def add():
#     print( 1234)
#     yield 1
#     return
#     yield 2
# a =add()
# print(next(a))
# print(next(a))
# from functools import reduce
# a = [1,2,3,4,5,6,7,8,9,9,8,76,5,4,34,3,2,21,1,2,23,3,4,3,32,2,3,34,4,3,2,]
# b = reduce(lambda x,y:x+y,a)
# print(b)
# c=0
# for i in a:
#     c+=i
# print(c)
# for i in a:
#     for b in a:
#         if i+b ==5:
#            print(i,b)
# a = {1,2,3,4,5,6,7}
# print(type(a))
# for i in a:
#     print(i)
# a.add(123)
# print(a)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


# a.insert(0,11)
# print(a)
# b = [1,2,3,4,5,6,76,8,9,89,8,8,8,8,8,8,8,8,88,87,7,7,7,7,7,67,6,6,6,65]
# a.extend(b)
# # print(a)
# a.append(11)
# print(a)
# del a
# print(a)
# pop删除返回被删除的元素
# print(a.pop(1))
# print(a)
# remove根据value删除 删除第一个匹配的内容
# print(a.remove(0))
# print(a)
# def fbl(coun):
#     index = 1
#     a, b = 0, 1
#     while index <= coun:
#         yield b
#         c = b
#         b = a + b
#         a = c
#         index += 1
#
#
# for i in fbl(8):
#     print(i)


# def fbl(count):
#     inde =1
#     a,b = 0,1
#     while inde <=count:
#         yield b
#         c= b
#         b = a+b
#         a = c
#         inde +=1
# for i in fbl(8):
#     print(i)
# def kugou_mius(sount):
#     index =1
#     while  index <= sount:
#         print(f"播放音乐{index}")
#         index +=1
#         yield None
#     raise StopIteration()
#
# def youku_move(sount):
#     index =1
#     while  index <= sount:
#         print(f"播放电影{index}")
#         index +=1
#         yield None
#     raise StopIteration()
# muzek = kugou_mius(20)
# move = youku_move(20)
# def main():
#     stop_muze =True
#     stop_move = True
#     while True:
#         try:
#             next(muzek)
#         except StopIteration:
#             print("音乐完了")
#             stop_muze =False
#         try:
#             next(move)
#         except StopIteration:
#             print("电影完了")
#             stop_move =False
#         if not stop_muze and stop_move:
#             break
# if __name__ =="__main__":
#     main()

# def pbl(data):
#     index =1
#     a,b = 0,1
#     while index <= data:
#         yield b
#         c= b
#         b = a+b
#         a = c
# a1 = pbl(10)
# for i in range(10):
#     print(next(a1))



# def pet(count):
#     index = 1
#     a,b =0,1
#     while index <= count:
#         yield b
#         c = b
#         b =b+a
#         a = b


class falsk:

    def __init__(self):
        self.view_url = {}

    def route(self,url):
        def out_wapper(fun):
            self.view_url[url] = fun.__name__
            def wapper(*args,**kwargs):
                fun(*args,**kwargs)
            return wapper
        return out_wapper


    def run(self):
        url = input("请输入你要访问的 url")
        view_data = self.view_url.get(url)
        if view_data:
            exec(view_data+"()")
        else:
            print("访问的页面不存在")
