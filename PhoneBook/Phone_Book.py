import json


class Book:
    def __init__(self, filepath):
        file = open(filepath)
        self.json_data = json.load(file)

    def display(self):
        for i in self.json_data:
            print(i)

    def add_entry(self):
        while True:
            name = input("Enter Name:")
            phonenumber = input("Enter Phone Number:")
            for i in self.json_data:
                if i["Name"] == name:
                    print("Name Already Exist!!")
                    break
                else:
                    dict1 = {}
                    dict1.__setitem__("Name", name)
                    dict1.__setitem__("PhoneNumber", phonenumber)
                    self.json_data.append(dict1)
                    return

    def delete_entry(self):
        while True:
            name = input("Enter Name:")
            for i in self.json_data:
                if i.get("Name") == name:
                    var = i
                    self.json_data.remove(var)
                    self.display()
                    return
            print(f"{name} is not present")

    def display_one(self,name):
        for i in self.json_data:
            if i.get("Name") == name:
                print(i)
                return
        print(f"{name} is not present")

    def update_entry(self):
        while True:
            name = input("Enter Name:")
            for i in self.json_data:
                if i.get("Name") == name:
                    data = i
                    while True:
                        option = int(input("What you want to update:\n1.Name\n2.Phone Number\n"))
                        if option == 1:
                            new_name = input("Enter new Name:")
                            data["Name"] = new_name
                            self.display_one(new_name)
                            return
                        if option == 2:
                            new_phone = int(input("Enter New Phone Number:"))
                            data["PhoneNumber"] = new_phone
                            self.display_one(name)
                            return
            print(f"{name} is not Present")



