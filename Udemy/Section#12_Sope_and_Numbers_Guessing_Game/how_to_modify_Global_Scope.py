
# Modifying Global Scope
#
# element = 1
#
# if element < 2:
#     element = 2
#     print(f"Element inside of if block: {element}")
#
# print(f"Element outside after if block {element}")



enemies = 1
def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

#########################################################################################

# if you want to change global variable from function
# But this is bad idea
global_varibale = 10

def change_function():
    global global_varibale
    global_varibale += 1
    print(f"inside function {global_varibale}")
change_function()
print(f"After function {global_varibale}")

# ##########################################################################################
#This is better solution of changing global variables

global_varibale = 10

def change_function():
    print(f"inside function {global_varibale}")
    return global_varibale + 1
global_varibale = change_function()
print(f"After function {global_varibale}")

