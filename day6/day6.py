def count_fish_in_buckets(buckets):
    sum = 0
    for v in buckets.values():
        sum += v
    return sum

def part1():
    lantern_fish = []

    with open("./long.txt", "r") as f:
        for line in f:
            lantern_fish = list(map(int, line.split(',')))
    print(lantern_fish)
    buckets = {}
    for i in range(0,9):
        buckets[i] = 0

    for fish in lantern_fish:
        buckets[fish] += 1

    for iteration in range(0,256):
        print(F'Day 0: {buckets}')
        bucket0 = buckets[0]
        bucket1 = buckets[1]
        bucket2 = buckets[2]
        bucket3 = buckets[3]
        bucket4 = buckets[4]
        bucket5 = buckets[5]
        bucket6 = buckets[6]
        bucket7 = buckets[7]
        bucket8 = buckets[8]


        buckets[0] += bucket1 - bucket0
        buckets[1] += bucket2 - bucket1
        buckets[2] += bucket3 - bucket2
        buckets[3] += bucket4 - bucket3
        buckets[4] += bucket5 - bucket4
        buckets[5] += bucket6 - bucket5
        buckets[6] += bucket0 - bucket6 + bucket7
        buckets[7] += bucket8 - bucket7
        buckets[8] += bucket0 - bucket8
    


    print(F'count of fish: {count_fish_in_buckets(buckets)}')
    

        
        

            




        
            







part1()