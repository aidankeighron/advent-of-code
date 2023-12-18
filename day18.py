from util import init, load_day, load_file, result
import math
import numpy as np
init()

array = load_day(18)
part_2 = False
total = 0

points = [(0,0)]
for line in array:
    direction, amount, color = line.split(" ")
    amount = int(amount)
    color = color.replace("(", "")
    color = color.replace(")", "")
    direction = int(color[-1])
    amount = int(color[1:-1], 16)
    if direction == 0:#"R":
        for _ in range(amount):
            points.append((points[-1][0]+1,points[-1][1]))
    if direction == 2:#"L":
        for _ in range(amount):
            points.append((points[-1][0]-1,points[-1][1]))
    if direction == 3:#"U":
        for _ in range(amount):
            points.append((points[-1][0],points[-1][1]-1))
    if direction == 1:#"D":
        for _ in range(amount):
            points.append((points[-1][0],points[-1][1]+1))
            
x = []
y = []
for p in points:
    x.append(p[0])
    y.append(p[1])
    
def poly_area(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

A = poly_area(x, y)
b = len(points)+1
I = A + 1 - b // 2
result(int(I+b))