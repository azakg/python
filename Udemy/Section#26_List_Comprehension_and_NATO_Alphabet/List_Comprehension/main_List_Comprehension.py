number = [1, 2, 3]
new_numbers = [n + 1 for n in number]
print(new_numbers)

name = "Azamat"

new_list = [latter for latter in name]
print(name[0])

#Example n+1

number = [n*2 for n in range(1,5)]
print(number)

################################################################################
# ____Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
upper_names = [name.upper() for name in names if len(name) > 5]
print(upper_names)
