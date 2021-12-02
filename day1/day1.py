
def part1():
    measurements = []
    with open("./long1.txt", "r") as f:
        for line in f: 
            measurements.append(int(line))

    increases = 0
    prev = measurements.pop(0)
    for m in measurements:
        if (m > prev):
            increases = increases + 1
        
            print ('m: ' , m, 'p: ', prev)
        else:
            print('m: ', m, 'decrease')
        prev = m
    print('part1: ', increases)

def part2():
    measurements = []
    with open("./short2.txt", "r") as f:
        measurements = [tuple(line.split()) for line in f]
    print(measurements[0][0])             



part1()
part2()
    

