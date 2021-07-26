# a = True
# b = False
# if a:
# 	print('执行了a')
# else:
# 	print('执行了else')
# if not a:
# 	print('执行了a')
# else:
# 	print('执行了else')

# 循环语句
# 99乘法表
a =0
while a <=9:
	b=1
	while b<=a:
		print(b,'*',a,'=',a*b,end='')
		b+=1
	print('  ')
	a+=1
		
a= 0
b=0
# 计算100以内偶数相加
while a <=100:
	if a % 2 == 0:
 		b+=a
	a+=1
print(b)
