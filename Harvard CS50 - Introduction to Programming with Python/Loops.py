# print("meow")
# print("meow")
# print("meow")

##################################
# while loop
##################################
# i = 0
# while i < 3:
#     print("meow")
#     i += 1 # same as i = i + 1

#################################
# for loop
#################################
# for i in [0,1,2]:
#     print("meow")
#
# for i in range(3):
#     print("meow")
#
# print("meow \n" + 3, end="")

##################################################
# simplified ( Combination of while and for loop)
##################################################
# while True: #infinite loop
#     n = int(input("What's n? "))
#     if n < 0:
#         continue #stay within this loop
#     else:
#         break #break you out of the recently began loop

# while True:  # infinite loop
#     n = int(input("What's n? "))
#     if n > 0:
#         break
#
# for _ in range (n):
#     print("meow")

# def main():
#     number = get_number()
#     meow(number)
#
# def get_number():
#     while True:
#         n = int(input("What's n? "))
#         if n > 0:
#             break
#     return n #not just to break out of the code but also to return a value in code. hands bach an actual value to the user
#              #can also use break but need to return the value
#              #return should be inside the function. return can be inside or oustide of the loop
#
# def meow(n):
#     for _ in range(n):
#         print("meow")

#main()

################################
# list
################################
#students = ["Hermione", "Harry", "Ron"]

# print(students[0])
# print(students[1])
# print(students[2])

# for student in students:
#     print(student)

####################################################
# function - len() tell you the length of the list
# function - range() it returns the range of value
####################################################

# for i in range(len(students)):
#     print(i+1, students[i])

######################################################################
# dict- Dictionary
#     - allows you to associate one value with another
#     - words and definition. associate something with something else
#     - collection of values
# Syntax: name = {key:value}
# allows actual words as your index
# if for loop is used it will iterate the keys
# None - Special keyword. capital N. Absence of a value
######################################################################

# students = {"Hermione": "Gryffindor",
#             "Harry": "Gryffindor",
#             "Ron": "Gryffindor",
#             "Draco": "Slytherin"
#             }

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# for student in students:
#     print(student, students[student], sep=", ") #separator of words for print

##########################
#dictionary inside a list
##########################
#
# students = [
#     {"name": "Hermione", "house": "Gryffindor", "patronus":"Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus":"Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus":"Jack Russell Terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None}
# ]
#
# for student in students:
#     print(student["name"], student["house"], student["patronus"], sep=(", "))


# print("#")
# print("#")
# print("#")
#
# for _ in range(3):
#     print("#")

# def main():
#     print_column(3)
#
# def print_column(height):
#     # for _ in range(height):
#     #     print("#")
#
#     print("#\n" * height, end="")
#
# main()

# def main():
#     print_row(4)
#
# def print_row(width):
#     print("?" * width)
#
# main()

def main():
    print_square(3)

# def print_square(size):
#     #for each row in square
#     for i in range(size):
#
#         #for each brick in row
#         for j in range(size):
#
#             #print brick in the row
#             print("#", end="")
#
#         #print next line
#         print()

# def print_square(size):
#     for i in range(size):
#         print("#" * size)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()