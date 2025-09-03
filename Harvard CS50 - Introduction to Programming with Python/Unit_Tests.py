##########################################################################################
# Unit Testing - testing individual units of a program. Test for function that was written
###########################################################################################

# def main():
#  #   x = int(input("What's x? "))
#     x = input("What's x? ")
#     print("x squared is", square(x))
#
# def square(n):
#     return n * n
#
# if __name__ == "__main__":
#     main()

##################################################################################
# assert - allow you to do something that is true. if false an error will display
# AssertionError
##################################################################################

def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world"):
#    print("hello,", to)
    return f"hello, {to}"

if __name__ == "__main__":
    main()

##########################################################
# packages - multiple modules organized inside a folder
# file __init__ - even if the file is empty. treat folder not just a module but a package. treat the folder as a packed
##########################################################
