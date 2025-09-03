evenNumbers={2,4,6,8,10}
#setOne={1,2,3,4,5}
#evenNumbers.add(12)
#evenNumbers.update([14,16,18,20])
#extension = [22,24,26,28]
#evenNumbers.update(extension)
#evenNumbers.remove(3)
#evenNumbers.discard(12)
#evenNumbers.pop()
#evenNumbers.clear()
#setTwo=evenNumbers.copy()
#oddNumbers={1,3,5,7,9,10}
#setTwo={3,4,5,6,7}
#numbers=evenNumbers.union(oddNumbers)
#setThree = setOne.difference(setTwo)
#setThree = setOne.intersection(setTwo)
#setThree = setOne.symmetric_difference(setTwo)
numbers={1,2,3,4,5,6,7,8,9,10}
#numbers=list(numbers)
#numbers[0]="Hatdog"
#numbers=tuple(numbers)
#numbers=set(numbers)

#print(evenNumbers)
#print(len(evenNumbers))
#print(setTwo)
print(numbers)
#print(setThree)
#print(evenNumbers.isdisjoint(oddNumbers))
#print(evenNumbers.issubset(numbers))
#print(numbers.issuperset(evenNumbers))