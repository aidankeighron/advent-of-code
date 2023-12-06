import time, math
from parse import compile, parse

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