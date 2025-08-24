import random
n = 20
li = random.sample(range(1, 101), n)

max_number = 0
for i in li:
    if i > max_number:
        max_number = i
    else:
        max_number = max_number

print(li)
print(max_number)