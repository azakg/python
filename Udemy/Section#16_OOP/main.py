# import another_module
#
# print(another_module.another_varible)
#
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("darkSeaGreen")
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)


# table.field_names = ["Azamat", "Nurzhamal", "Tamchy", "Altai"]
# table.add_row([38, 33, 9, 5])
# print(table)