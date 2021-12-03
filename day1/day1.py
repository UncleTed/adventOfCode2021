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


def letters():
    a = 97
    count = 0
    while 1:
        yield chr(a)
        a = a + 1

def part2():
    gen = letters()
    count = 1
    with open("./short1.txt", "r") as f:
        measurements = [(line.split()) for line in f]
    letter = gen.__next__()
    print(measurements.pop(0), letter)
    for m in measurements:
        if (count % 3 == 0):
            letter = gen.__next__()
        print(m, letter)    
        count = count + 1

        
            

part1()
part2()

    


