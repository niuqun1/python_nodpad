# 变量：相当于一个容器来存储值得。
# 定义变量
name = "python"
print(name)
print(id(name))
name = "python1"
print(name)
print(id(name))
# 内存地址不会发生变化
name1 = name
print(id(name1))
# 如果某个变量是第一次赋值，那么会新建一个变量并且赋值
# 若果某个变量不是第一次赋值，那么会多这个变量重新赋值
# 如果一个变量从来没有出现过直接使用会报错
# 变量的命名规则
	# 1 大小写敏感 a 跟A 是两个不同的变量名
	# 2小驼峰命名法 userAge
	# 3 大驼峰命名法 UserAge
	# 4 下划线命名法 user_age
	# 5 不可使用关键字命名 `and`、`or`、`def`、`class`、`import`、`print`、`return`等关键字不能作为变量名来使用。、
	# 6 不可以数字开头入 1username
# type函数的使用：type函数是用来查看变量的数据类型如 type(user_name)
user_name = 18
print(type(user_name))
user_name1 = 18.2
print(type(user_name1))
user_name2 = '我是字符串'
print(type(user_name2))
# 返回type
print(type(type))
# 基本数据类型
	# 输入 input 接收到的参数永远都是字符串
	# 字符串相加得到字符串
	# 字符串与数字相加 得到字符串
	# 数字相加得到数字
	# 数据类型转换
	# 字符串转换数字时值不能有符号或字母汉字 只能是整数包含-数、
num1 = '-1'
print(int(num1))
 # 小数转换整数过滤小数点后面的数
num_fola = 3.141592653
print(int(num_fola))
num_5 = 5
num_2 = 2
# 算数运算符
print(num_5 // num_2)

# 格式化输入
age =  25
name = 'alix'
weight = 142.5
print('他的名字是%s他的年龄是%d他的体重是%f'%(name,age,weight))
print(f"他的名字是{name}他的年龄是{age}他的体重是{weight}")
print("他的名字是{}他的年龄是{}他的体重是{}".format(name,age,weight))

# 算数运算符
# +：加号运算符：
num1 = 142
num2 = 58
str_num = "100"
sun = num1+num2
print(sun)

# -：减号运算符：
num1 = 142
num2 = 58
str_num = "100" 
sun = num1 - num2
print(sun)

# *：乘号运算符。
num1 = 142
num2 = 58
str_num = "100"
sun = num1 * num2
print(sun)

# /：除法运算符：
num1 = 142
num2 = 58
str_num = "100"
sun = num1 / num2
print(sun)


# //：取整除：
num1 = 142
num2 = 58
str_num = "100"
sun = num1 // num2
print(sun)


# %：取余：
num1 = 142
num2 = 58
str_num = "100"
sun = num1 % num2
print(sun)

# **：幂运算：


# +=：a+=1等价于a=a+1。

# -=：a-=1等价于a=a-1。

# *=：a*=2等价于a=a*2。

# /=：a/=2等价于a=a/2。

# %=：a%=2等价于a=a%2。

# **=：a **= 2等价于a = a**2。

# //=：a //= 2等价于a = a//2。

