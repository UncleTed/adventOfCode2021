from collections import Counter

# this doesn't work at all

def part1():
    counter =  Counter()
    with open("./short.txt") as f:
        row = 0
        for line in f:
            l = line.strip()
            col = 0
            for c in l:
                counter[row, col] = c
                col += 1
            row += 1
    print(counter[0,0])

part1()