#  案例1：求1-10之间的和。
# print(123)
# a=0
# b=0
# while a<=10:
#     b += a
#     a+=1
# print(b)
# b1=0
# for i in range(10):
#     b1 += i
# print(b)


# 3. 案例2：统计'python papijiang papa mama'中p出现的个数。
# sta_count = 'python papijiang papa mama'
# a=0
# b=0
# while a<len(sta_count):
#     if sta_count[a] == 'p':
#         b += 1
#     a+=1
# print(b)

# a1=0
# for n in sta_count:
#     if n == 'p':
#         a1 += 1
#     else:
#         pass
# print(a1)

# 4. 案例3：九九乘法表。
# a=0
# while a<=9:
#     b=1
#     while b<=a:
#         print(b,a)
#         b+=1
#     a+=1
for i in range(1,10):
    for b in range(1,i+1):
        print(b,i)
    

