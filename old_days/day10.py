from util import init, load_day, load_file, result
import math
init()

array = load_day(10)
part_2 = False
total = 1

start = (0,0)
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == "S":
            start = (i, j)
            break
    if start != (0,0):
        break
    
# current = [start, (start[0], start[1]-1)]
current = [start, (start[0]+1, start[1])]
# previous = start
while array[current[-1][0]][current[-1][1]] != 'S':
    total += 1
    char = array[current[-1][0]][current[-1][1]]
    previous = current[-2]
    # print(char)
    if char == '|':
        if previous[0] < current[-1][0]:
            current.append((current[-1][0]+1, current[-1][1]))
        else:
            current.append((current[-1][0]-1, current[-1][1]))
    if char == '-':
        if previous[1] > current[-1][1]:
            current.append((current[-1][0], current[-1][1]-1))
        else:
            current.append((current[-1][0], current[-1][1]+1))
    if char == 'L':
        if previous[0] == current[-1][0]-1:
            current.append((current[-1][0], current[-1][1]+1))
        else:
            current.append((current[-1][0]-1, current[-1][1]))
    if char == 'J':
        if previous[0] == current[-1][0]-1:
            current.append((current[-1][0], current[-1][1]-1))
        else:
            current.append((current[-1][0]-1, current[-1][1]))
    if char == '7':
        if previous[0] == current[-1][0]+1:
            current.append((current[-1][0], current[-1][1]-1))
        else:
            current.append((current[-1][0]+1, current[-1][1]))
    if char == 'F':
        if previous[0] == current[-1][0]+1:
            current.append((current[-1][0], current[-1][1]+1))
        else:
            current.append((current[-1][0]+1, current[-1][1]))
    if char == '.':
        break

from shapely.geometry import Polygon
import numpy as np
import cv2

image = np.ones((150, 150, 1))*255
polygon = Polygon(current) # Assuming the OP's x,y coordinates

cv2.drawContours(image, [np.array(current)], -1, (0,0,0), 1)
# print(current)
cv2.imshow("test", cv2.resize(image, (150*5, 150*5)))
cv2.waitKey(0)

print(polygon.area)
print(polygon.length)
print(polygon.length**0.5)
# 7421x=443
# 26x=8
print(8/26)
print(443/7421)


result(total//2)
result(total//2)