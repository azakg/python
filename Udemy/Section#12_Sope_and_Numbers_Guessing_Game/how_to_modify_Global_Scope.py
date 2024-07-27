
# Modifying Global Scope
enemies = 1
def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")


element = 1

if element < 2:
    element = 2
    print(f"Element inside of if block: {element}")

print(f"Element outside after if block {element}")
