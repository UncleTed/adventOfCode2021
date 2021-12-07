from collections import Counter
import statistics
def part1():
    crab_submarines = []

    with open("./long.txt", "r") as f:
        for line in f:
            crab_submarines = list(map(int, line.split(',')))
    most_common_position = Counter(crab_submarines).most_common(1)[0]
    print(Counter(crab_submarines).most_common(5))
    print(F'Median: {statistics.median(crab_submarines)}')
    print(F'Most common postion: {most_common_position}')
    most_common_position = 330
    fuel = 0
    for c in crab_submarines:
        fuel += abs(c - most_common_position)
            
    print(F'Fuel used: {fuel}')
    # 459589 is too high
    # 430623 is still too high

if __name__ == '__main__':
    part1()