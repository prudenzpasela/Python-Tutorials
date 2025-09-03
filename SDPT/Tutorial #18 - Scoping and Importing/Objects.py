class Students:
    def __init__(self,name,course):
        self.name=name
        self.course=course

    def intro(self):
        print("I'am "+ self.name + " a " + self.course)
