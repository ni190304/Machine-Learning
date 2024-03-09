#Exercise!
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

# Solution1

for row in picture:
    for pixel in row:
        if(pixel):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
    
# Solution2

for row in range(len(picture)):
    for pixel in range(len(picture[row])):
        if(picture[row][pixel]):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()