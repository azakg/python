#sorting elements alphabetic order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# revers order soring in alphabetic order
print("#################################################################")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print("This sorting in alphabetic order")
print(cars)

#Temporary soring
print("#################################################################")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list again: ")
print(cars)

#Revers order but not in alphabetic order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"\nThis is original order: \n{cars}")
cars.reverse()
print("\nThis is just in revers order, not in alphabetic: ")
print(cars)

#Print length of the list
print(len(cars))