import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(800, 600)

# Create the turtle
river = turtle.Turtle()
river.speed(0)

# Draw the river
river.penup()
river.goto(-400, -200)
river.pendown()
river.color('blue')
river.begin_fill()
river.forward(800)
river.right(90)
river.forward(100)
river.right(90)
river.forward(800)
river.right(90)
river.forward(100)
river.end_fill()

# Exit on click
screen.exitonclick()
