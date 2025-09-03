# class Person:
#     def __init__(self, name):
#         self.name = name
#        # print(self.name + " Created!")
#
#     def intro(self):
#         print("I'am " + self.name)

# name = input("Enter name: ")
# p1 = Person(name)
#
# p1 = Person("David")
# p2 = Person("Alenere")
# p3 = Person("Jay")
# p4 = Person("Josh")
#
# listofpeople = [p1,p2,p3,p4]
#
# #listofpeople[1].intro()
#

#Using loop to read collections

# for person in listofpeople:
#     print(person.name)

#Using loop to write in collections

# listofpeople = []
#
# for i in range(5):
#     name = input("Enter name: ")
#     p = Person(name)
#     listofpeople.append(p)
#
# #print(listofpeople)
#
# for person in listofpeople:
#     person.intro()

#Student Registration Program
# Create a program that will let the user register students as long as the like.
# Make it so that after the finished registering students, all of the students information will be diplayed
# using an object function
# students should have a constructor and the following attributes
# Name
# Course
# Year
# Section
# and an object Function
# introduce()
# Output:
# Student #1
# Name: David Sdpt
# Course: BSIT
# Year: 1
# Section: E
#
# Student #2
# Name: Alen Sdpt
# Course: BSCS
# Year: 2
# Section: A

class Student:
    def __init__(self, name, course, year, section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section

    def introduce(self):
        print(" Name   : " + self.name)
        print(" Course : " + self.course)
        print(" Year   : " + self.year)
        print(" Section: " + self.section)

studentlist = []

inputstudent = input("Would you like to enter a student? Y/N: ")



while True:
    name = input("Enter name    : ")
    course = input("Enter course  : ")
    year = input("Enter year    : ")
    section = input("Enter section: ")
    p = Student(name, course, year, section)
    studentlist.append(p)
    print()

    inputagain = input("Would you like to enter another student? [Y/N]: ")

    if inputagain == "Y" or inputagain == "y":
        pass
    else:
        break

i=1
for student in studentlist:
    print()
    print("Student #" + str(i))
    student.introduce()
    i = i + 1