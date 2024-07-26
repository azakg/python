
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# Localj Scope ##########################################################################################
def drink_potion():
    portion_strength = 2  # This variable is accessible just inside of the function
    print(portion_strength)

drink_potion()

##########################################################################################

# Global Scope #########################################################################

player_health = 10

def drink_potion2():
    potion_strength = 2
    print(player_health)

drink_potion2()