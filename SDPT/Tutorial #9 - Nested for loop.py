# for x in range(5):
#     print("hello")

# for x in range(3):
#     for y in range(3):
#         print("*")

# for x in range(5):
#     for y in range(5):
#         print("*",end="")
#     print()

# students = [
#     ["bsit", "ale"],
#     ["bsit", "dave"],
#     ["bscs", "jay"],
#     ["bscs", "eman"],
#     ["bsit", "pat"]
#]
#print(students[0][1])

# for x in students:
#     for i in x:
#         print(i)
#     print()

students = [
    ["bsit", ["david", "ale"]],
    ["bscs", ["jay", "eman", "pat"]],
    ["blis", ["kris", "bob", "john"]]
]

for i in students:
    print(i[0])
    for x in i[1]:
        print(" -" + x)
    print()
