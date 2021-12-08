from collections import Counter
from os import stat
import statistics
def part1():
    crab_submarines = []

    with open("./short.txt", "r") as f:
        for line in f:
            crab_submarines = list(map(int, line.split(',')))
    median_position = int(statistics.median(crab_submarines))
    print(F'Median position: {median_position}')
    fuel = 0
    for c in crab_submarines:
        fuel += abs(c - median_position)
            
    print(F'Fuel used: {fuel}')
    # 459589 is too high
    # 430623 is still too high

# 0 1 2 4 7 14 16
def part2():
    with open("./long.txt", "r") as f:
        for line in f:
            crab_submarines = list(map(int, line.split(',')))

    fuel = []
    low = min(crab_submarines)
    high = max(crab_submarines)

    
    for position in range(low, high + 1):
        ff = 0
        for c in crab_submarines:
            ff += sum(range(abs(c - position)+1))
        fuel.append(ff)
    print(fuel)
    print(F'Part 2: {min(fuel)}')

# part 2 86397082 is too high
#        86396960 is too low
#        86397080
if __name__ == '__main__':
    part1()
    part2()