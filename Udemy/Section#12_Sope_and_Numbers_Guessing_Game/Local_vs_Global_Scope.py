#
# enemies = 1
#
# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")
#
#
# # Localj Scope ##########################################################################################
# def drink_potion():
#     portion_strength = 2  # This variable is accessible just inside of the function
#     print(portion_strength)
#
# drink_potion()
# print(portion_strength) # This is error, you couldn't call variable inside of the function
#
#
#
# # Global Scope #########################################################################
#
# player_health = 10
#
# def drink_potion2():
#     potion_strength = 2
#     print(player_health) # With Global variable you can call from everywhere
#
# drink_potion2()


# There is no Block Scope ##########################################################################################

if 3 > 2:
    a_variable = 10

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]
print(new_enemy) # Here you can note that "new_enemy is available outside of the if block"


