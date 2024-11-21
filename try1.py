import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")


# Create turtle object
flower = turtle.Turtle()
flower.speed(0)
flower.color("purple")


# Function to draw a petal
def draw_petal():
    flower.circle(50, 60)
    flower.left(120)
    flower.circle(50, 60)
    flower.left(120)

# Draw flower
flower.penup()
flower.goto(0, -50)
flower.pendown()
for _ in range(6):
    draw_petal()
    flower.right(60)

# Finish
flower.hideturtle()
turtle.done()
