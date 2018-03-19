from turtle import *
from draw_a_square import *

coord_list = [(-100, -100), (100, 100), (-100, 100), (100, -100)]

for coord in coord_list:
    up()
    home()
    x, y = coord
    setheading(270)
    forward(x)
    setheading(0)
    forward(y)
    down()
    draw_square()

    mainloop()