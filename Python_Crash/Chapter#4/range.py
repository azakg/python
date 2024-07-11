for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

numbers1 = []
for value in range(1, 11):
    numbers1.append(value)
print(min(numbers1))
print(max(numbers1))
print(sum(numbers1))

#Short version of the previous code
squares = [value **2 for value in range(1, 11)]
print(squares)