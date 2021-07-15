class Pet:

    def __init__(self, pet_id, pet_name, pet_type, pet_price):
        self.pet_id = pet_id
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.pet_price = pet_price

    def get_pet(self):
        return f"{self.pet_id}&{self.pet_name}&{self.pet_type}&{self.pet_price}\n"

    @classmethod
    def read_pet_data(cls, link):
        pet_id, pet_name, pet_type, pet_price = link.replace("/n", '').split("&")
        pet = Pet(pet_id, pet_name, pet_type, pet_price)
        return pet


class Petmanager:
    __instance = None
    __filename = "pet_datas.txt"

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Petmanager, cls).__new__(cls, *args, **kwargs)
            return cls.__instance

    def add_pet(self, pet_id, pet_name, pet_type, pet_price):
        with open(Petmanager.__filename, 'w') as fp:
            pet = Pet(pet_id, pet_name, pet_type, pet_price)
            fp.writelines(pet.get_pet())

    def read_pet(self):
        all_pet = []
        with open(Petmanager.__filename, 'r') as fp:
            for link in fp:
                all_pet.append(Pet.read_pet_data(link))
            return all_pet


class Applivation:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Applivation, cls).__new__(cls, *args, **kwargs)
            return cls.__instance

    def __inpet_pet_info(self):
        pet_id = input("请输入宠物id")
        pet_name = input("请输入宠物名字")
        pet_type = input("请输入宠物种类")
        pet_price = input("请输入宠物价格")
        pet_maneger.add_pet(pet_id, pet_name, pet_type, pet_price)

    def __print_pet(self):
        data = pet_maneger.read_pet()
        for link in data:
            print("宠物id：{}宠物名字：{}宠物类别{}宠物价格{}".format(link.pet_id, link.pet_name, link.pet_type, link.pet_price))

    def run(self):
        print("*" * 30)
        print("0推出系统")
        print("*" * 30)
        print("1添加宠物")
        print("*" * 30)
        print("2现实所以宠物")
        print("*" * 30)
        while True:
            option = input("请输入操作菜单")
            if option == "o":
                break
            elif option == "1":
                self.__inpet_pet_info()
            elif option == "2":
                self.__print_pet()

pet_maneger = Petmanager()
app = Applivation()
app.run()