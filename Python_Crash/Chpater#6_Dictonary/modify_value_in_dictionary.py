alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")


print("\n########################################################################")
print("""For a more interesting example, let’s track the position of an alien that can
"move at different speeds. We’ll store a value representing the alien’s current
"speed and then use it to determine how far to the right the alien should move:\n""")

alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_1['x_position']}")

#Move the alien to the right.
# Determine how far to move the alien vased on this current speed
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_1['x_position'] = alien_1['x_position' ] + x_increment

print(f"New position: {alien_1['x_position']}")
