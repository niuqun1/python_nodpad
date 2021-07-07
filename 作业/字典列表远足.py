a = [1,2,3,4,5,6,7,8,9]
# a.reverse()
# print(a)
print(a[::-1])
# 学生管理系统
# 添加学生
user_data = []
def add_studic():
    studic_data = {}
    id = input("请输入学生编号")
    name = input("请输入学生姓名")
    sex =input("请输入学生性别")
    studic_data["id"] = id
    studic_data["name"] = name
    studic_data["sex"] = sex
    user_data.append(studic_data)
    return studic_data

def print_data(user_data):
    for  user in user_data:
        print(f"学生编号：{user['id']}学生姓名：{user['name']}学生性别：{user['sex']}")

def del_user_Data(user_data):
    user_id = input("请输入要删除的id")
    for user in user_data:
        if user["id"] == user_id:
            user_data.remove(user)
            print_data(user_data)

def serch(user_data):
    user_id = input("请输入要查询的id")
    for user in user_data:
        if user["id"] == user_id:
            print(f"学生编号：{user['id']}学生姓名：{user['name']}学生性别：{user['sex']}")



add_studic()
add_studic()            

print_data(user_data)
del_user_Data(user_data)
serch(user_data)



