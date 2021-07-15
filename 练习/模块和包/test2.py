import sys,os
print("test2" in sys.modules)

from test1 import  *
print(sys.modules)

print("我是test2")
# 1 判断os.models中是否有test1
# 2 判断内存中是否有 test2
# 3