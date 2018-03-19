star = '*'
space = ' '
tHeight = int(raw_input("Height? "))
base = (tHeight * 2) - 1
for row in range(1, tHeight + 1):
    spaces = tHeight - row
    stars = (row * 2) - 1
    print (space * spaces) + (star * stars)
