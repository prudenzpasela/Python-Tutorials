studentOneAttributes = {
    "height":172,
    "weight":48,
    "skin":"brown"
}

studentOne = {
    "name":"SDPT",
    "course":"BSIT",
    "age":18,
    "physical": studentOneAttributes
}

studentTwo = {
    "name":"John",
    "course":"BSCS",
    "age":19
}

#studentOne["name"] = "bebang"
#studentOne["gender"] = "Male"
#studentOne.pop("name")
#studentOne.popitem()
#studentOne.clear()
#studentCopy = studentOne.copy()
#students = [studentOne, studentTwo]


print(studentOne)
#print(studentCopy)
#print(studentOne["name"])
#print(studentOne.get("name"))
#print(studentTwo["course"])
print(len(studentOne))
print(studentOne.keys())
print(studentOne.values())
#print(students)
#print(students[0].get("name"))
print(studentOne.get("physical"))
print(studentOne.get("physical").get("height"))