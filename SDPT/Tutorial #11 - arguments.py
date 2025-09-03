# def sayHello(name):
#     print("hello, " + name)
#
# sayHello(input("Enter Name: "))

# def sayHello(*names):
#     for name in names:
#         print(" Hello, " + name)
#
# sayHello("SDPT", "dave", "jett", "ale", "bob")

# def sayHello(firstname, lastname):
#         print(firstname + " " + lastname)
#
# sayHello(lastname="Solutions",firstname="sdpt")

# def printFamily(*fnames, lname):
#     for name in fnames:
#         print(name + " " + lname)
#
#
# printFamily("john", "bob", "Jett", lname="hatdog")


# def printstudent(**student):
#     print(student["name"])
#     print(student["course"])
#     print(student["age"])
#     print(student["average"])
#     print(student["coursecode"])
#
# printstudent(name="SDPT", age=18, course="BSIT", average=90, coursecode=101)

def summationof(*numbers):
    sum = 0
    for num in numbers:
        sum += num #sum = sum + num
    return sum

print(summationof(1,2,3,4,5,6,7,8,9,10))