import time, math
from parse import compile, parse
import numpy as np, datetime, os, time
# https://plotly.com/python/
import plotly.express as px

times = {}
def profile(name):
    def decorate(fn):
        def wrapper(*args, **kwargs):
            start = time.time_ns()
            result = fn(*args, **kwargs)
            if name not in times:
                times[name] = []
            times[name].append((time.time_ns() - start)/1_000_000)
            print(f'{name}: {np.average(times[name])}')
            return result
        return wrapper
    return decorate

def box_poly_area(poly, includes_start=True):
    area = poly_area(poly)
    border = len(poly) - (1 if includes_start else 0)
    return (area + 1 - border // 2) + border

def lcm(xs):
  ans = 1
  for x in xs:
    ans = (ans*x)//math.gcd(x,ans)
  return ans

def poly_area(poly: list[int, int]) -> int:
    return poly_area(*zip(*poly))
    

def poly_area(x_coords: int, y_coords: int) -> int:
    return 0.5*np.abs(np.dot(x_coords,np.roll(y_coords,1))-np.dot(y_coords,np.roll(x_coords,1)))

def load_file(file: str, char: bool = False) -> list:
    with open(file, 'r') as file:
        if char:
            file_content = [list(line) for line in file.read().split()] 
            return file_content
        else:
            file_content = file.read().split('\n')
            if file_content[-1] == '':
                del file_content[-1]
            return file_content

def graph_points(points: list) -> None:
    x_coords, y_coords = zip(*points)
    fig = px.scatter(x=x_coords, y=y_coords)
    fig.show()

def print_points(points: list, width: int, height: int, flipped: bool = False) -> None:
    image = ['.' for _ in range(width) for _ in range(height)]
    for point in points:
        point = point[::-1] if flipped else point
        image[point[0]][point[1]] = '#'
    for i in image:
        print(''.join(i))

def load_day(day: int, year: int = datetime.datetime.now().year, char: bool = False) -> list:
    return load_file(f'./{year}/txt/day{day}.txt', char)

def format(input: str, pattern: str):
    p = compile(pattern)
    result = p.parse(input)
    return result.fixed

def flatten(x):
    return [j for i in x for j in i]
    
start = 0
def init():
    global start
    start = time.time_ns()
    
def result(total: int = 0):
    duration_ns = time.time_ns()-start
    if duration_ns / 1_000_000_000 < 2:
        print(f'Answer: {total} Time: {round(duration_ns / 1_000_000, 2)}ms')
    else:
        print(f'Answer: {total} Time: {round(duration_ns / 1_000_000_000, 2)}s')