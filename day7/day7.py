from collections import Counter
import statistics
def part1():
    crab_submarines = []

    with open("./long.txt", "r") as f:
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


def part2():
    with open("./long.txt", "r") as f:
        for line in f:
            crab_submarines = list(map(int, line.split(',')))

if __name__ == '__main__':
    part1()