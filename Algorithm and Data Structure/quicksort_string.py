# import sys
# from load import load_strings

# names = load_strings(sys.argv[1])

names = ["Francina Vigneault", "Lucie Hansman", "Nancie Rubalcaba", "Elida Sleight", "Guy Lashbaugh",
                "Ginger Schlossman", "Suellen Lauces", "Jamey Kirchgesler", "Amiee Elwer", "Lacresha Peet"]

def quicksort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

sorted_names = quicksort(names)
for n in sorted_names:
    print(n)

"""
python quicksort_string.py > sorted.txt
"""
