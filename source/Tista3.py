
import turtle

crazy = 'crazy'
normal = 'normal'

name = input('Enter your name:')
color = int(input('Would you like 6, 7, or 8 colors'))

name = turtle.Turtle()
name.shape('turtle')

if color == 6:
    color0 = input('Choose a color: ')
    color1 = input('Choose a color: ')
    color2 = input('Choose a color: ')
    color3 = input('Choose a color: ')
    color4 = input('Choose a color: ')
    color5 = input('Choose a color: ')
    colors = [color0, color1, color2, color3, color4, color5]
   
if color == 7:
    color0 = input('Choose a color: ')
    color1 = input('Choose a color: ')
    color2 = input('Choose a color: ')
    color3 = input('Choose a color: ')
    color4 = input('Choose a color: ')
    color5 = input('Choose a color: ')
    color6 = input('Choose a color: ')
    colors = [color0, color1, color2, color3, color4, color5, color6]
   

if color == 8:
    color0 = input('Choose a color: ')
    color1 = input('Choose a color: ')
    color2 = input('Choose a color: ')
    color3 = input('Choose a color: ')
    color4 = input('Choose a color: ')
    color5 = input('Choose a color: ')
    color6 = input('Choose a color: ')
    color7 = input('Choose a color: ')
    colors = [color0, color1, color2, color3, color4, color5, color6, color7]

type_of_circle = input('Do you want like a sort of crazy color circle or just a normal one with overlapping colors ? If you want the normal one type normal, if you want the sort of weird one type crazy: ')

if type_of_circle == crazy:
    for each_color in colors:
        angle = 360 / len(colors)
        name.color(each_color)
        name.circle(40)
        name.right(angle)
        name.forward(30)
        for each_color in colors:
            angle = 180 / len(colors)
            name.color(each_color)
            name.circle(40)
            name.right(angle)
            name.forward(30)
           
if type_of_circle == normal:
    for each_color in colors:
        angle = 360 / len(colors)
        name.color(each_color)
        name.circle(40)
        name.right(angle)
        name.forward(30)
        for each_color in colors:
            angle = 360 / len(colors)
            name.color(each_color)
            name.circle(40)
            name.right(angle)
            name.forward(30)


