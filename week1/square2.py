width = int(raw_input("how wide is the box"))
height = int(raw_input("how tall is the box"))

for x in range(height):
    if row == 0:
      print "*" * width 
    elif row == height -1 == height:
        print "*" * width
    else:
        output = ''
        for column in range(width):
            if columc == 0:
                ouput = '*'
            elif column - 1 == width:        