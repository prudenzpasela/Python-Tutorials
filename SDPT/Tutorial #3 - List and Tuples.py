#LISTS
#+INDEX -    0       1        2
#-INDEX -   -3      -2       -1
#courses = ["BSIT", "BSCS", "BLIS", "Hatdog", "Cheesedog", "BSCC", "BSCE"]
#courses[0] = "Hatdog"
#courses.append("hatdog")
#courses.insert(1,"Hatdog")
#courses.remove("BSIT")
#courses.pop()
#courses.pop(1)
#del courses[0]
#del courses
#courses.clear()
#x = courses.copy()
#food = ["Hatdog", "Cheesedog"]
#alphabet = ["Z", "A", "C", "B"]
#coursefood = courses + food
#courses.append(food)
#courses.reverse()
#alphabet.sort()
#alphabet.sort(reverse=True)
#+INDEX -    0       1        2              3
#courses = ["BSIT", "BSCS", "BLIS",["Hatdog", "Cheesedog"]]
#+INDEX -    0       1        2                      3
#courses = ["BSIT", "BSCS", "BLIS",[["Shampoo", "alcohol"],"Cheesedog"]]


#print(courses)
#print(courses[1:4])
#print(courses[:4])
#print(courses[2:])
#print(len(courses))
#print(courses.count("BSCS"))
#print(x)
#print(courses+food)
#print(coursesfood)
#print(courses)
#print(food)
#print(alphabet)
#print(courses[3])
#print(courses[3][0])
#print(courses[3][0][1])
#print(courses[3][1])

#TUPLES
#+INDEX -    0       1        2
#courses = ("BSIT", "BSCS", "BLIS") convert to list
courses = ["BSIT", "BSCS", "BLIS"]
#courses[0] = "hatdog" will error cannot be changed
#courses = list(courses)
courses = tuple(courses)

print(courses)