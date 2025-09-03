
#Parent Class
class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def intro(self):
        print("Hi I'am " + self.fname + " " + self.lname)

    def introlname(self):
        print("Hi i am " + self.lname)

#Child Class
# class student(Person):
#     pass
#
# p1 = Person("David","Sdpt")
# p1.intro()
#
# s1 = student("Alenere", "Solution")
# s1.intro()

#Child Class Overriding Constructor and adding Attributes
class student(Person):
    def __init__(self,fname,lname, sectionyear):
        super().__init__(fname,lname)
        self.sectionyear = sectionyear

# p1 = Person("David","SDPT")
# s1 = student("Alenere", "SDPT", "E-1")

#Child Class Overriding Functions
    # def intro(self):
    #     print("Hi I'am "+ self.fname + " " + self.lname + " from " +self.sectionyear)

# p1 = Person("David", "SDPT")
# s1 = student("Alenere", "SDPT", "E-1")

# p1.intro()
# s1.intro()

#Customizing Overrode Function
    def intro(self):
        #print("From " + self.sectionyear)
        super().intro()
        print("From " + self.sectionyear)

#Adding Function
    def saysection(self):
        print(self.sectionyear)

# p1 = Person("David","SDPT")
# s1 = student("Alenere", "SDPT", "E-1")
# p1.intro()
# s1.intro()
# s1.saysection()

class Employee(Person):
    def __init__(self,fname,lname,salary):
        super().__init__(fname,lname)
        self.salary = salary

    def intro(self):
        super().intro()
        print("My Salaray is " + str(self.salary))

    def saySalary(self):
        print("Salary: "+ str(self.salary))

p1 = Person("David","SDPT")
s1 = student("Alenere", "SDPT", "E-1")
e1 = Employee("Pat", "Makara", 50000)
p1.intro()
s1.intro()
s1.saysection()
s1.introlname()
e1.intro()
e1.saySalary()
e1.introlname()

