import turtle

construtor = turtle.Turtle()

x = 100

construtor.begin_fill()
construtor.fillcolor('green')
for i in range(5):
    construtor.forward(x)
    construtor.right(72)
    construtor.forward(x)
    construtor.left(144)
construtor.end_fill()

turtle.done()
