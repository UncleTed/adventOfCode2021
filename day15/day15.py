
from functools import reduce

grid = {}
visited = [[0,0]]


grid_height = 9
grid_width = 9

def neighbor(x, y):
    neighbors = []
    if x >= 0 and x < grid_width :
        neighbors.append([x+1, y])
    if y >= 0 and y < grid_height:
        neighbors.append([x,y+1])
    
    return neighbors

def part1():
    with open('./short.txt') as f:
        row = 0
        for line in f:
            col = 0
            for l in line.strip():
                grid[col,row] = int(l)
                col += 1
            row += 1

    print(grid)
    x = 0
    y = 0

    
    total_risk = 0
    total_risk += grid[0,0]
    print('Start at [0,0] -> 1')
    while x < grid_width and y < grid_height:
        neighbors = neighbor(x, y)
        # print(f'neighbors: {neighbors}')
        unvisited = [item for item in neighbors if item not in visited]
        smallest = reduce(lambda a,b: a if grid[a[0],a[1]] < grid[b[0],b[1]] else b, unvisited)
        # print(smallest)
        x = smallest[0]
        y = smallest[1]
        visited.append([x,y])
        print(f'Current: {x},{y} -> {grid[x,y]}')
        total_risk += grid[x,y]
    print(f'total: {total_risk}')


# 681 is too high
part1()