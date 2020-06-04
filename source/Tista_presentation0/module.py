import turtle

color = input('Enter a color: ')
color0 = input('Enter a color: ')
color1 = input('Enter a color: ')

Tista = turtle.Turtle()
turtle.shape('turtle')

def triangle(color, color0, color1):
    Tista.color(color)
    Tista.forward(100)
    Tista.color(color0)
    Tista.left(120)
    Tista.forward(100)
    Tista.color(color1)
    Tista.left(120)
    Tista.forward(100)
    turtle.done()
    
