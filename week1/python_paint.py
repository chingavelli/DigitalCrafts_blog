def drawSquare(width, height):
    print '*' * width
    num_space = width -2
    spaces = ' ' * num_spaces
    for i in range(height -2 ):
        print '*' + spaces + '*'
    print '*' * width


def drawTraingle(height):
    base = height * 2 - 1 
    for row in range(1, height + 1):
        spaces = height - row
        print " " * spaces + "*" * (row * 2 - 1)

def drawBox(width, height):
    for row in range(height):
        if row == 0:
            print "*" * width
        elif row == height - 1:
            print "*" * width
        else: 
            spaces = width - 2
            print "*" + " " + spaces + "*"  

            drawSquare(5, 5)
            drawTriang(10)
            drawBox(10, 4)                    