# class Animal:
#     def __init__(self, type, voice):
#         self.type=type
#         self.voice=voice
#
#     def speak(self):
#         print(self.voice)
#
#     def introduceSelf(self):
#         print("I am a " + self.type)
#
# aOne = Animal("Dog", "Arf")
# aTwo = Animal("Cat", "Meow")
#
# aOne.speak()
# print(aOne.voice)
# aOne.introduceSelf()
# aTwo.introduceSelf()
# aTwo.speak()

# firstName
# lastName
# likesCount
# friendsName[LIST]
#
# introduce
# Hi i'am' {firstName}{lastName}
#
# fullprofile
# Full NameError
# Likes
#
# friends
#     -Alenere
#     -Jay
#     -Josh
#     _pat

class socmed:

    def __init__(self, fname, lname, likes, friends):
        self.fname = fname
        self.lname = lname
        self.likes = likes
        self.friends = friends

    def intro(self):
        print("Hi i'am " + self.fname + " " + self.lname)

    def fullprofile(self):
        print("Full Name: " + self.fname + " " + self.lname)
        print("Likes: " + str(self.likes))
        print("Friends: ")
        for friends in self.friends:
            print("   -" + friends)


profile = socmed("prudenz", "pasela", 10, ["Ale", "Jay", "Josh", "Pat"])

print("Introduce")
profile.intro()

print("Full Profile")
profile.fullprofile()

