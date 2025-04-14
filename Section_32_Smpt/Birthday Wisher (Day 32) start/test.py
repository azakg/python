import random
import os

# def random_line(afile):
#     line = next(afile)
#     for num, aline in enumerate(afile, 2):
#         if random.randrange(num):
#             continue
#         line = aline
#     return line

lines = open('quotes.txt').read().splitlines()
myline = random.choice(lines)

print(myline)