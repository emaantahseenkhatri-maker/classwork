import turtle

turtle.Screen().bgcolor("blue")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

import turtle

turtle.Screen().bgcolor("purple")

board = turtle.Turtle()
 
# Triangle
board.forward(100)
 
board.left(120)
board.forward(100)
 
board.left(120)
board.forward(100)


# Square
board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

board.forward(100)
board.left(90)


import turtle

turtle.Screen().bgcolor("lightblue")
board = turtle.Turtle()
 
# first triangle for star
board.forward(100) # draw base
 
board.left(120)
board.forward(100)
 
board.left(120)
board.forward(100)
 
board.penup()
board.right(150)
board.forward(50)
 
# second triangle for star
board.pendown()
board.right(90)
board.forward(100)
 
board.right(120)
board.forward(100)
 
board.right(120)
board.forward(100)
 
turtle.done()