players = ['charles', 'martina', 'michael', 'florence','eli']
print(players[-3:])

#Looping through a Slice
players = ['charles', 'martina', 'michael', 'florence','eli']
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(friend_foods)
friend_foods.append("ice cream")
print(my_foods)
print(friend_foods)