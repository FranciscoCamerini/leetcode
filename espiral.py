import turtle

construtor = turtle.Turtle()

x = 10

for i in range(200):
    construtor.forward(x + i)
    construtor.left(95)

turtle.done()
