#age = int(input("enter your age: "))

#if age >= 18:
#    print("Legal Age")
#elif age >=13:
#    print("Teenager")
#else:
#   print("Too young")


 #  print("Thank you for using the program")
#print("Thank you for using the program")

#password = input("Enter Password: ")

#if password == "123abc":
#    print("Access Granted")
#else:
#    print("Access Denied")

#age = int(input("enter your age: "))
# height = int(input("enter your height"))
#
# if age >= 18:
#     if height >= 176:
#         print("tall and legal age")
#     elif height >= 150:
#         print("average and legal age")
#     else:
#         print("short and legal age")
# else:
#     print("too young")

# age = int(input("enter your age: "))
#
# if not age >= 18:
#    print("Too young")
# else:
#     print("Legal age")

# age = int(input("enter your age: "))
# height = int(input("enter your height"))
#
# if age >= 18 and height >= 176:
#         print("tall and legal age")
# elif age >= 18 and height >= 150:
#         print("average and legal age")
# elif age >= 18:
#         print("short and legal age")
# else:
#         print("too young")

# username = input("Enter Username: ")
# password = input("Enter Password: ")
#
# if username == "SDPT" and password == "admin":
#     print("welcome SDPT")
# elif username == "Solutions" and password == "admin123":
#     print("welcome solutions")
# else:
#     print("invalid credentials")

# hasStick = True
# hasRuler = False
#
# if hasStick or hasRuler:
#     print("pasok")
# else:
#     print("labas")

#bag = ["wallet", "gun", "lipstick", "computer", "laptop"]
# bag = ["lipstick", "computer", "laptop"]
#
# if "gun" in bag or "wallet" in bag:
#     print("huli")
# else:
#     print("pasok")

math = float(input("enter math grade: "))
science = float(input("enter science grade: "))
arts = float(input("enter arts grade: "))
grade = (math + science + arts) / 3

print(grade)

if grade >= 98 and grade <= 100:
    print("With Highest Honor")
elif grade >= 95:
    print("With High Honors")
elif grade >= 90:
    print("With Honors")
elif grade >= 75:
    print("Passed")
elif grade >= 51 and grade <=74:
    print("Failed")
else:
    print("Invalid Grade")

# if grade >100 or grade <=50:
#     print("Invalid Grade")
# elif grade >= 98:
#     print("With Highest Honors")
# elif grade >= 95:
#     print("With High Honors")
# elif grade >= 90:
#     print("With Honors")
# elif grade >= 75:
#     print("Passed")
# else:
#     print("Failed")