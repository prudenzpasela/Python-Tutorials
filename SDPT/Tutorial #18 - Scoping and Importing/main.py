#Global Variable
# y = "World"

# #pwede i access sa loob ng function. pwede i access sa buong file
# #kahit sa loob ng conditional at loop statements
#
# #Local Variable
# def sayHello():
#     x = "Hello"
#     print(x)
#     print(y)
#
# #print(x)
# #hindi pwede i access sa labas ng function. eto ung local variable sa loob lang ng function pwede ma access
# #also work withs conditional statement at loop ung mga naka indent lang ung pwede ma access
#
# sayHello()
#
# #Parameter Variable
# def say(word): #ung word local lang din sya pero hindi initialize sa loob ng function. dineclare na agad sa loob ng function
#     print(word)#pwede pa i access dito kasi local pa sya
#
# #print(word) #hindi pwede i access ung word
# say("what")

#Global Keyword
# def say():
#     global y # na aappektuhan na nito ung y variable sa labas. kaya ung y sa loob nag bago na din
#     y = "Hello" #local variable na to
#     print(y)
#
# say()
# print(y)

# import arithmetic as a
# import constants as c
# import Objects as o

# from Other_folder.arithmetic import add as a
# from Objects import Students

# print(arithmetic.add(5,2))
# print(constants.pi)
#
# s1 = Objects.Students("David", "BSIT")
# s1.intro()

# c.pi
# a.add(5, 2)
# o.Students("dave", "BSCS")

# print(a(5,2))
# print(Students("dave","bsit"))

import Other_folder.arithmetic
#import Other_folder.arithmetic as add
#from Other_folder.arithmetic import add

print(Other_folder.arithmetic.add(5,2))
