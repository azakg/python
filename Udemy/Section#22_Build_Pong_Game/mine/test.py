import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
follower = turtle.Turtle()
follower.shape("turtle")
follower.color("blue")
follower.speed(0)  # Set the turtle speed to the maximum

# Define the function to move the turtle
def follow_mouse():
    x, y = screen.cv.winfo_pointerxy()
    follower.goto(0, screen.window_height() // 2 - y)
    screen.ontimer(follow_mouse, 10)  # Continue checking mouse position every 10 ms

# Start following the mouse
follow_mouse()

# Keep the window open
turtle.done()
