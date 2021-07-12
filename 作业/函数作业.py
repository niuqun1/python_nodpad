def add(a,b):
    return a+b
data = add(4,5)
print(data)
print(add(4,5))
def adds(*args):
    for i in args:
        i+=i
    return i
print(adds(1,2,3))