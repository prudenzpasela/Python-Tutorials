# import sys
# from load import load_strings

# names = load_strings(sys.argv[1])

names = ["Francina Vigneault", "Lucie Hansman", "Nancie Rubalcaba", "Elida Sleight", "Guy Lashbaugh",
                "Ginger Schlossman", "Suellen Lauces", "Jamey Kirchgesler", "Amiee Elwer", "Lacresha Peet"]

search_names = ["Francina Vigneault", "Elida Sleight", "Guy Lashbaugh",
                "Amiee Elwer", "Lacresha Peet"]

def index_of_item(collection, target):
    for i in range(0, len(collection)):
        if target == collection[i]:
            return i
    return None
for n in search_names:
    index = index_of_item(names, n)
    print(index)