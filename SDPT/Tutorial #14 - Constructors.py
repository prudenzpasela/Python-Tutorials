# class Character:
#     def __init__(self):
#         print("Character Created")
#
# charOne = Character()
# charTwo = Character()
# charThree = Character()

class Character:
    def __init__(self, name, hp, mp, atk, lvl):
        self.name=name
        self.hp=hp
        self.mp=mp
        self.atk=atk
        self.lvl=lvl
        print("Created " + self.name)

charOne = Character("David",200,100,15,2)
charTwo = Character("Alenere",300,200,16,3)
