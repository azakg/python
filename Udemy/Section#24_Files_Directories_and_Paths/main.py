# Reading file ###############################################################################################
from pathlib import Path
print("This is with close method")
file = open('my_file.txt')
contents = file.read()
print(contents)
file.close()
print()

with open("my_file.txt") as file:
    print("This is with out close method")
    contents = file.read()
    print(contents)
print()

print("This is with path")
path = Path("my_file.txt")
contents = path.read_text()
print(contents)
##################################################################################################################

#Writing file ###############################################################################################
with open("my_new_file.txt", mode="a") as file:
    file.write("\nNew text3.")



