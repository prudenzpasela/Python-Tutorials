###############################################
# set - collection of values without duplicates
# global - global variable if you put at the top of the file
# constants - variable cannot be change or modify
# type hints -
# mypy - checking if code is adhering to your type hint
# pip install mypy
# docstrings - standardize how to document functions
# Command line Arguments
# -n number of times
# argparse - library handles parsing of command line arguments
# unpacking - splitting and putting it into 2 variable
#           - use * at the beginning of the variable and will unpack
#           - two * when unpacking dictionary to pass the key and value separated by = sign
# * or **   - visual indication when a function might variable take variable number of arguments
# map       - allow you to map that applies some function to every element of some sequence like a list
# list comprehensions - construct list on a fly without using a loop
# filter - same effect as map but more functional feature
# dictionary comprehensions - create on a fly a dictionary with key and values
# enumerate - iterating over some sequence but finding out not each value one at a time but both value and index
# generators - generate values from functions
#            - it can still generate a massive amount of data for your users but return a little bit of data at a time
# yield      - tell python to return just 1 value at a time of this loop
# iterators  - return for loop to iterate generated values one at a time
################
# houses.py

# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"}
# ]
#
# # houses = []
# # for student in students:
# #     if student["house"] not in houses:
# #         houses.append(student["house"])
#
# houses = set()
# for student in students:
#     houses.add(student["house"])
#
# for house in sorted(houses):
#     print(house)

###########
# bank.py

# balance = 0
#
# def main():
#     print("Balance:", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance:", balance)
#
# def deposit(n):
#     global balance
#     balance += n
#
# def withdraw(n):
#     global balance
#     balance -= n
#
# if __name__ == "__main__":
#     main()

###########
# OOP

# class Account:
#     def __init__(self):
#         self._balance = 0
#
#     @property
#     def balance(self):
#         return self._balance
#
#     def deposit(self, n):
#         self._balance += n
#
#     def withdraw(self, n):
#         self._balance -= n
#
# def main():
#     account = Account()
#     print("Balance:", account.balance)
#     account.deposit(100)
#     account.withdraw(50)
#     print("Balanace:", account.balance)
#
# if __name__ == "__main__":
#     main()

####################
# meows.py
# MEOWS = 3
#
# MEOWS = 4
#
# for _ in range(MEOWS):
#     print("meow")

######
# OOP
#
# class Cat:
#     MEOWS = 3
#
#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")
#
# cat = Cat()
# cat.meow()

########################
# Another Method - mypy

# def meow(n: int) -> None:
#     for _ in range(n):
#         print("meow")
#
# number: int = int(input("Number: "))
# meows: str = meow(number)
# #meow(number)
# print(meows)

###########################
# Another method
# def meow(n: int) -> str:
#     return "meow\n" * n
#
# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")

###########################
# Docstring
# def meow(n: int) -> str:
#     """Meow n times."""
#     """
#     Meow n times.
#
#     :param n: Number of time to meow
#     :type n: int
#     :raise TypeError: If n is not an int
#     :return: A string of n meows, one per line
#     :rtype: str
#     """
#     return "meow\n" * n
#
# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")

########################
# Command line Arguments
# -n number of times
# import sys
#
# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("usage: meows.py")

########################
# argparse
# import argparse
#
# parser = argparse.ArgumentParser(description="Meow like a cat")
# parser.add_argument("-n", default=1, help="number of times to meow", type=int)
# args = parser.parse_args()
#
# # for _ in range(int(args.n)):
# #     print("meow")
#
# for _ in range(args.n):
#     print("meow")

############
# unpack.py
# first, last = input("What's your name? ").split(" ")
# print(f"hello, {first}")

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts
#
# #coins = [100,50,25]
# coins = {"galleons":100, "sickles":50, "knuts":25}
#
# #print(total(100,50,25), "Knuts")
# #print(total(coins[0], coins[1], coins[2]), "Knuts")
# #print(total(*coins), "Knuts")
# #print(total(galleons=100, sickles=50, knuts=25), "Knuts")
# #print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
# print(total(**coins), "Knuts")

#################
# * or **
# def f(*args, **kwargs):
#     #print("Positional: ", args)
#     print("Name:", kwargs)
#
# # f(100,50,25)
# # f(100,50,25,5)
# # f(100 )
#
# f(galleons=100, sickles=50, knuts=25)

###############
# yell.py
# def main():
#     #yell("This is CS50")
#     #yell(["This", "is", "CS50"])
#     yell("This", "is", "CS50")

#def yell(phrase):
#   print(phrase.upper())

# def yell(words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)

# def yell(*words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)

#########
# Map
# def yell(*words):
#     uppercased = map(str.upper, words)
#     print(*uppercased)

###################
# list comprehension
# def yell(*words):
#     uppercased = [word.upper() for word in words]
#     print(*uppercased)
#
# if __name__ == "__main__":
#     main()

#################
# gryffindors.py
# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]

# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]
#
# for gryffindor in sorted(gryffindors):
#     print(gryffindor)

# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"

# gryffindors = filter(is_gryffindor, students)

# gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)
#
# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])

##########################
# Dictionary Comprehension

students = ["Hermione", "Harry", "Ron"]

# gryffindors = []
#
# for student in students:
#     gryffinsors.append({"name": student, "house": "Gryffindor"})

# list comprehension
#gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# dictionary comprehension
# gryffindors = {student: "Gryffindor" for student in students}
#
# print(gryffindors)

###########
# Enumerate
# for student in students:
#     print(student)
#
# for i in range(len(students)):
#     print(i+1, students[i])
#
# for i, student in enumerate(students):
#     print(i+1, student)

#############
# sleep.py
def main():
    n = int(input("What's n? "))
    # for i in range(n):
    #     #print("🐑" * i)
    #     print(sheep(i))
    for s in sheep(n):
        print(s)

# def sheep(n):
#     #return "🐑" * n
#     flock = []
#     for i in range(n):
#         flock.append("🐑" * i)
#     return flock

############
# yield
def sheep(n):
    for i in range(n):
        yield "🐑" * i

if __name__ == "__main__":
    main()