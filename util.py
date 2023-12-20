import time, math
from parse import compile, parse
import numpy as np

def box_poly_area(poly, includes_start=True):
    area = poly_area(poly)
    border = len(poly) - (1 if includes_start else 0)
    return (area + 1 - border // 2) + border

def lcm(xs):
  ans = 1
  for x in xs:
    ans = (ans*x)//math.gcd(x,ans)
  return ans

def poly_area(poly):
    x, y = [], []
    for p in poly:
        x.append(p[0])
        y.append(p[1])
    return poly_area(x,y)
    

def poly_area(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

def load_file(file: str, char: bool = False) -> list[list[str]] | list[str]:
    with open(file, 'r') as file:
        if char:
            file_content = [list(line) for line in file.read().split()] 
            return file_content
        else:
            file_content = file.read().split('\n')
            if file_content[-1] == '':
                del file_content[-1]
            return file_content

def load_day(day: int, char: bool = False) -> list[list[str]] | list[str]:
    return load_file(f'./txt/day{day}.txt', char)

def format(input: str, pattern: str):
    p = compile(pattern)
    result = p.parse(input)
    return result.fixed

def flatten(x):
    return [j for i in x for j in i]
    
format("Game 1: 10 10 10", "Game {}: {} {} {}")

start = 0
def init():
    global start
    start = time.time()
    
def result(total: int = 0):
    print(f'Answer: {total} Time: {"%.2f"%(time.time()-start)}')