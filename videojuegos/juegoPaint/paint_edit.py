"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
import math
from freegames import vector

t = Turtle() # make a new turtle

def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    "Draw circle from start to end."
    a = math.sqrt((start.x-end.x)**2+(start.y - end.y)**2)  # make de area of the circle  
    hideturtle()
    begin_fill()
    t.circle(a) # use a function to make the circle with the area 
    end_fill()


def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    forward(end.x*2 - start.x*2) #change the size of the of the one side of the shape
    left(90) #change the direccion of the vector
    
    forward(end.x - start.x) #use the normal size of the square
    left(90)
    
    forward(end.x*2 - start.x*2) #change the size of the of the other side of the shape
    left(90)
    
    forward(end.x - start.x)#use the normal size of the square

    end_fill()


def triangle(start, end):
    #the same base as the square
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(3):
        forward(end.x - start.x)
        left(120) #It use a change of 120° to make different angles

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('#00FFFF'), 'A')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
