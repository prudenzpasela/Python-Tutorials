# age = 1
#
# while age < 18:
#     print("Still young: " + str(age))
#     age = age + 1
# else:
#     print("Legal age: " + str(age))

#Index          0       1         2       3
# studentID = [2000123, 2000124, 2000125, 2000126, 2000127, 2000128, 2000129]
# i = 0
#
# while i < len(studentID):
#     print(studentID[i])
#     i = i + 1

# while True:
#     print("Hello World")
#     break

# print("Crush ka ba ng crush mo? ")
# while True:
#     answer = input("Answer: ")
#     if answer == "hindi":
#         print("correct")
#         break
#     else:
#         print("mali")

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]

#even number divisible by 2
#odd number is not divisible by 2
# Modulo % - remainder

# i = 0
#
# while i < len(numbers):
#     if (numbers[i] % 2 == 0):
#         print("Even number: " +str(numbers[i]))
#     else:
#         print("Odd number: " +str(numbers[i]))
#     i = i+1


print("What is 1 + 1")
chances = 3

while chances > 0:
    answer = input("Answer: ")
    if answer == "2":
        print("correct")
        break
    else:
        print("wrong")
        chances = chances - 1
else:
    print("you lose")
