import turtle

construtor = turtle.Turtle()
construtor.color('orange')

x = 15

for i in range(0, 14, 2):
    construtor.begin_fill()
    construtor.fillcolor('orange')
    construtor.circle(x + i)
    construtor.end_fill()
    construtor.up()
    construtor.forward(2 * (x + i) + 2)
    construtor.down()

turtle.done()
