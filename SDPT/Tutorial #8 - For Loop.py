
#           x          x         x
fruits = ["Apple", "Banana", "Orange", "Grapes", "Avocado"]

#for every x in fruits
# for x in fruits:
#     print(x)
#     break
# # else:
#     print("No More Fruits")

# for x in fruits:
#     print(x)
#     if x == "Banana":
#         break

# for x in fruits:
#     print(x)
#     if x == "Apple":
#         print("An apple a day keeps the doctor away")
#     elif x == "Orange":
#         print("Oragnes!!!")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#even number divisible by 2 remainder = 0
#odd number is not divisible by 2 remainder !=0
#modulo %

# for number in numbers:
#     if number % 2 == 0:
#         print("Even Number: " + str(number))
#     else:
#         print("Odd Number: " + str(number))

# for x in range(10):
#     print(x)

# for x in range(5):
#      print("hello world")



username = ["John", "Alenere", "David"]
password = ["abc123", "123abc", "hahatdog"]

username1 = input("Enter username: ")
password1 = input("Enter password: ")

for x in range(len(username)):
    if username1 == username[x] and password1 == password[x]:
        print("Welcome, " + username[x])
        break
else:
    print("Account not found")