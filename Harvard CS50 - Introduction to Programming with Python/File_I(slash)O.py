# #############################
# File I/O - Input Output file
#
# name = input("What's your name? ")
# print(f"hello, {name}")
#
# names = []
#
# for _ in range (3):
#     names.append(input("What's your name? "))
#
# for name in sorted(names):
#     print(f"hello, {name}")
#
#
#
# ################################################
# open - function to open a file
#      - can read or write to the file
#      - "w" for write
#      - file will be created if not yet existing
#      - "a" for append
#      - "r" for read
# close - function to close and save the file
# ################################################
#
# name = input("What's your name? ")
#
# file = open("students.csv", "a")
# file.write(f"{name}\n")
# file.close()
#
# ##########################################
# with - automatically open and close file
# ##########################################
#
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")
#
# #################
# Another method
#
# with open("names.txt", "r") as file:
# #     lines = file.readlines()
# #
# # for line in lines:
# #     print("hello,", line.rstrip())
#     for line in file:
#         print("hello,", line.rstrip())
#
# ###############
# Another method
#
# names = []
#
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
#
# for name in sorted(names):
#     print(f"hello, {name}")
#
# ###############
# Another method
#
# with open("names.txt") as file:
#     for line in sorted(file):
#         print("hello,", line.rstrip())
#
#
# ##############################################################
# if we want to make changes and iterate over it before sorting
# names = []
#
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
#
# for name in sorted(names, reverse=True):
#     print(f"hello, {name}")
#
# split - function to split any character and tell what character to use
#
# with open("students.csv") as file:
#     for line in file:
#        # row = line.rstrip().split(",")
#        # print(f"{row[0]} is in {row[1]}")\
#        name, house = line.strip().split(",")
#        print(f"{name} is in {house}")
#
# ################
# Another method
# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")
#
# for student in sorted(students):
#     print(student)
#
#
# ################
# Another method
# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         # student = {}
#         # student["name"] = name
#         # student["house"] = house
#         student = {"name": name, "home": home}
#         students.append(student)
#
# # def get_name(student):
# #     return student["name"]
# #    # return  student["house"]
# #
# # ####################################################################################################
# # # lambda = a function that just has no name or anonymous. if you are only going to use it at 1 place
# # ####################################################################################################
# #
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

################
# Another method
# import csv
#
# students = []
#
# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         #print(row)
#         #students.append({"name": row[0], "home": row[1]})
#         students.append({"name": name, "home": home})
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

##################
# Another method
# import csv
#
# students = []
#
# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row['name'], "home": row['home']})
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

##################################################
# store name and home and keep adding to the file
# import csv
#
# name = input("What's your name? ")
# home = input("Where's your home ")
#
# # with open("students.csv", "a") as file:
# #     writer = csv.writer(file)
# #     writer.writerow([name, home])
#
# with open("students.csv", "a") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "home"])
#     writer.writerow({"name": name, "home": home})

###################################################################
# PIL
# pillow.readthedocs.io
# pillow - navigate image file and perform operations on image file

import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "customes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)