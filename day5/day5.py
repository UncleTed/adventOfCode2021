from collections import namedtuple



def is_vertical(line):
    s = slope(line[0], line[1])
    return s == None

def is_horizontal(line):
    s = slope(line[0], line[1])
    if ( s == None):
        return False
    return abs(s) == 0.0


def on_the_line(line1, p1):       #check whether p is on the line or not
   if  ( p1[0] <= max(line1[0][0], line1[1][0]) and
         p1[0] <= min(line1[0][0], line1[1][0]) and
        (p1[1] <= max(line1[0][1], line1[1][1]) and
         p1[1] <= min(line1[0][1], line1[1][1]))):
        return True;
   
   return False;
    
def direction(p1, p2 ,p3):
    val = (p2[1]-p1[1])*(p3[0]-p2[0])-(p2[0]-p1[0])*(p3[1]-p2[1])
    if (val == 0):
        return 0     #colinear
    elif(val < 0):
        return 2;    #anti-clockwise direction
    return 1        #clockwise direction


def is_intersect(line1, line2):
    dir1 = direction(line1[0], line1[1], line2[0])
    dir2 = direction(line1[0], line1[1], line2[1])
    dir3 = direction(line2[0], line2[1], line1[0])
    dir4 = direction(line2[0], line2[1], line1[1])
    if (dir1 != dir2 and dir3 != dir4):
        return True         #they are intersecting
    if(dir1==0 and on_the_line(line1, line2[0])):  #hen p2 of line2 are on the line1
        return True

    if(dir2==0 and on_the_line(line1, line2[1])): #when p1 of line2 are on the line1
        return True

    if(dir3==0 and on_the_line(line2, line1[0])): #when p2 of line1 are on the line2
        return True

    if(dir4==0 and on_the_line(line2, line1[1])): #when p1 of line1 are on the line2
        return True
         
    return False

def slope(p1, p2):
    numerator = p2[1] - p1[1]
    denominator = p2[0] - p1[0]
    if ( denominator == 0):
        return None
    return numerator / denominator

def part1():
    lines = []

    with open("./short.txt", "r") as f:
        for line in f:
            split = line.rstrip().split(' -> ')
            lines.append([tuple(map(lambda x: int(x), split[0].split(','))), tuple(map(lambda x: int(x), split[1].split(',')))])
        grid = {}
        for l in lines:
            if (is_horizontal(l)):
                print(F'H {l}')
                min_x = min(l[0][0], l[1][0])
                max_x = max(l[0][0], l[1][0])
                y = l[0][1]
                for x in range(min_x, max_x+1):
                    try:
                        grid[F'{x},{y}'] = grid[F'{x},{y}'] + 1
                    except KeyError:
                        grid[F'{x},{y}'] = 1
                
                        
            elif (is_vertical(l)):
                print(F'V {l}')
                min_y = min(l[0][1], l[1][1])
                max_y = max(l[0][1], l[1][1])
                x = l[0][0]
                for y in range(min_y, max_y+1):
                    try:
                        grid[F'{x},{y}'] = grid[F'{x},{y}'] + 1
                    except KeyError:
                        grid[F'{x},{y}'] = 1
            else:
                # if(l[0][0] - l[1][0] == l[0][1] - l[1][1]):  # slope is positive
                if((l[1][0] - l[0][0]) >0 and  (l[1][1] - l[0][1])>0):
                    print(F'D: {l}')
                    y = l[0][1]                                    
                    for x in range(l[0][0], l[1][0]+1):
                        try:
                            grid[F'{x},{y}'] = grid[F'{x},{y}'] + 1
                        except KeyError:
                            grid[F'{x},{y}'] = 1
                        y = y +1
                elif (l[0][0] - l[1][0] == -1* (l[0][1] - l[1][1])):
                    print(F'other D: {l}')
                    x = l[0][0]
                    for y in range(l[0][1], l[1][1]-1, -1):
                        try:
                            grid[F'{x},{y}'] = grid[F'{x},{y}'] + 1
                        except KeyError:
                            grid[F'{x},{y}'] = 1  
                        x = x + 1
                else:       # negative slope
                    y = l[0][1]                                    
                    for x in range(l[0][0], l[1][0]-1, -1):
                        try:
                            grid[F'{x},{y}'] = grid[F'{x},{y}'] + 1
                        except KeyError:
                            grid[F'{x},{y}'] = 1
                        y = y - 1



        print(grid)
        counter = 0
        for v in grid.values():
            if( v > 1):
                counter += 1
        print(counter)
part1()