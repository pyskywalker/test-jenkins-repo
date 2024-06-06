import turtle
import random

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("black")
tree = turtle.Turtle()
tree.hideturtle()
tree.speed(0)
tree.color("green")

# Function to draw a fractal tree
def draw_tree(t, branch_length, angle, depth):
    if depth == 0:
        return

    # Draw the main branch
    t.pensize(branch_length / 10)
    t.forward(branch_length)

    # Draw the right subtree
    t.right(angle)
    draw_tree(t, branch_length - random.randint(10, 20), angle, depth - 1)

    # Draw the left subtree
    t.left(angle * 2)
    draw_tree(t, branch_length - random.randint(10, 20), angle, depth - 1)

    # Move back to the original position and orientation
    t.right(angle)
    t.backward(branch_length)

# Position the turtle at the bottom center of the screen
tree.penup()
tree.goto(0, -screen.window_height() / 2 + 50)
tree.pendown()
tree.left(90)

# Draw the fractal tree
draw_tree(tree, 100, 20, 7)

# Keep the window open
turtle.done()
