##########################################################
# Exception - problems in your code
#            - if something has gone wrong in the program
##########################################################

##########################################
# SyntaxError - entirely on you to solve
#             - go back to your code
#             - must be fixed
##########################################

#print("hello , world)



#############################################################
# f string or format string
# to plug in the value of x
# to substitute what x actually is inside the curly brace
#############################################################

# x = int(input("What's x? "))
# print(f"x is {x}")

###############################################################################
# Try - try to do something and check something exceptional or erroneous happen
# except - exception of the error
###############################################################################

# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")

# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

# ValueError - value of someone type is incorrect
# NameError - refer to your code. you are doing something to your variable that you shouldn't

# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
#
# print(f"x is {x}")
#
####################################
# Another option to write the code
# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         print(f"x is {x}")

####################################
# Another option to write the code
# while True:
#     try:
#         x = int(input("What's x? "))
#         break
#     except ValueError:
#         print("x is not an integer")
#
# print(f"x is {x}")

# Using as a function
# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             break #break out of loop
#     return x #return value or hand back a value
####################################
# Another option to write the code
# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x #will not only you out of the loop but will also return a value

#####################################################
# Another option to write the code
# using fewer lines but too complicated to understand
# have a good reason when writing a code
# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")

################################
# pass - catch it but ignore it
################################
# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#            pass

#main()

#############################################################################################
# caller (main) doesn't have to know what the callee is naming its variable and vice versa
# caller - to call a function means to use it. is the function that is using it
# callee - the function being called
# Another option to write the code
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()

