from dataclasses import dataclass

def part1():
    measurements = []
    with open("./long.txt", "r") as f:
        for line in f: 
            measurements.append(int(line))

    increases = 0
    prev = measurements.pop(0)
    for m in measurements:
        if (m > prev):
            increases = increases + 1
        
            # print ('m: ' , m, 'p: ', prev)
        # else:
            # print('m: ', m, 'decrease')
        prev = m
    print('part1: ', increases)



# Move the pointer
#  1 2 3 4 5 6 
#  ^ ^ ^
#    ^ ^ ^ 
#      ^ ^ ^ 


def sumOfNextThree(start, measurements):
    sum = 0
    for i in range(start, start + 3):
        sum = sum + measurements[i]
    return sum

    
def part2():
    increases = 0
    count = 0
    measurements = []
    with open("./long.txt", "r") as f:
        for line in f:
            measurements.append(int(line))

    current = 0
    prev = sumOfNextThree(0,measurements)
    print(prev)
    measurements.pop(0)
    i = 0
    while (i < len(measurements)-2):
        current = sumOfNextThree(i, measurements)
        print(current)
        if ( current > prev):
            print('c: ', current, 'p: ', prev)
            increases = increases + 1
        i = i + 1
        prev = current
        
    print('increases ', increases)

part1()
part2()

    


