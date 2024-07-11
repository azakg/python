#sorting elements alphabetic order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# revers order soring
print("#################################################################")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
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