
#def main():
    # name = get_name()
    # house = get_house()
    # name, house = get_student()
    # student = get_student()
    #print(f"{name} from {house}")

    # List
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"
    #print(f"{student[0]} from {student[1]}")

    # Dictionary
    # if student["name"] == "Padma":
    #     student["house"] = "Ravenclaw"
    # print(f"{student['name']} from {student['house']}")

# def get_name():
#     return input("Name: ")
#
# def get_house():
#     return  input("House: ")

# Tuple - return with comma or ()
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return name, house

# List - return with bracket
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house]

#################
# Another Method
# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student

#################
# Another Method
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house": house}
#
# if __name__ == "__main__":
#     main()

###########################################################################################
# classes - blueprint for pieces of data or object. can mold you can define and give a name
#         - when used you get a types of data that are designed what you want
#         - create or invent your own data types and give a name
#         - can have functions built inside a class
#         - will always have one argument called self
#         - represent when using real world entity
# objects - create object from classes
#         - when you use the blueprint or mold to create an object
#         - instances of classes
# attribute - instance variables inside of an object
# methods - functions you can define and behave in a special way
#         - allow you to determine behavior in a certain way
# __init__ - instance method
#          - if you want to initialize the contents of an object from a class
# raise    - raise all exception when you caught errors
# __str__  - special method will automatically call function anytime others wants to see your function as a string
# properties - is an attribute that has more functionality to prevent programmer for messing things up
# @properties - function @ syntax
# decorator - function that modify the behavior of other functions
# Getter and Setter - functions for error correction
# type() - to check what is the type
# class methods - same functionality associated with the class no matter what the object or value
# @classmethod - a method that has no access to self but know what class is inside
# Static method -
# @staticmethod -
# inheritance - Design your classes into hierarchy fashion. One class can inherit or borrow attributes methods or variables
# super() - accessing the super class
# operator overloading - can use symbols and implement your own interpretation
# object.__add__(self, other) - working for any object self = left of +, other = right of +.
#                             - add 2 vaults
######################################################################################################

# class Student:
#     def __init__(self, name, house):
#         # if not name:
#         #     raise ValueError("Missing name")
#         # if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#         #     raise ValueError("Invalid house")
#         self.name = name
#         self.house = house
#     #     #self.patronus = patronus
#     #
#     def __str__(self):
#         return f"{self.name} from {self.house}"
#
#     @classmethod
#     def get(cls):
#         name = input("Name: ")
#         house = input("House: ")
#         return cls(name, house)
    #
    # # Getter -
    # @property
    # def name(self):
    #     return self._name
    #
    # # Setter
    # @name.setter
    # def name(self, name):
    #     if not name:
    #         raise ValueError("Missing name")
    #     self._name = name


    # Getter
    #@property
    # def house(self):
    #     return self._house

    # Setter
    # @house.setter
    # def house(self, house):
    #     if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
    #         raise ValueError("Invalid house")
    #     self._house = house

    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "🐴"
    #         case "Otter":
    #             return "🦦"
    #         case "Jack Russel Terrier":
    #             return "🐶"
    #         case _:
    #             return "😒"
# def main():
#     #student = get_student()
#     student = Student.get()
#     #print(f"{student.name} from {student.house}")
#     #student.house = "Number Four, Privet Drive"
#     print(student)
#     # print("Expecto Patronum!")
#     # print(student.charm())


# def get_student():
#     student = Student()
#     student.name = input("Name :")
#     student.house = input("House: ")
#     return student

####################
# Simplified Method
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     #patronus = input("Patronus: ")
#     return Student(name, house)



# if __name__ == "__main__":
#     main()

#########
# Hat.py
# import random
# class Hat:
#     #def __init__(self):
#     #self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
#
#     #Class variable
#     houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
#
#     @classmethod
#     def sort(cls, name):
#         print(name, "is in", random.choice(cls.houses))
#
#     # def sort(self, name):
#     #     print(name, "is in", random.choice(self.houses))
#
# # hat = Hat()
# # hat.sort("Harry")
#
# Hat.sort("Harry")

############
# wizard.py
# class Wizard:
#     def __init__(self, name):
#         if not name:
#             raise ValueError("Missing name")
#         self.name = name
#
#     ...
#
# class Student(Wizard):
#     def __init__(self, name, house):
#         super().__init__(name)
#         # if not name:
#         #     raise ValueError("Missing name")
#         # self.name = name
#         self.house = house
#
#     ...
#
# class Professor(Wizard):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#
#     ...
#
# wizard = Wizard("Albus")
# student = Student("Harry", "Gryffindor")
# professor = Professor("Severus", "Defense Against the Dark Arts")

###########
# vault.py
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

potter = Vault(100, 50, 25)
print(potter)

weasly = Vault(25, 50, 100)
print(weasly)

# galleons = potter.galleons + weasly.galleons
# sickles = potter.sickles + weasly.sickles
# knuts = potter.knuts + weasly.knuts
#
# total = Vault(galleons, sickles, knuts)
total = potter + weasly
print(total)