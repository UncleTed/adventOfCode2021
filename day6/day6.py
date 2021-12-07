

def part1():
    lantern_fish = []

    with open("./short.txt", "r") as f:
        for line in f:
            lantern_fish = list(map(int, line.split(',')))
    print(lantern_fish)
    for day in range(1,257):
        f =[]
        new_fish = []
        print(F'Day {day}')
        for l in lantern_fish:
            if(l == 0):
                f.append(6)
                new_fish.append(8)
            else:
                f.append(l -1)
        lantern_fish = f + new_fish
        print(len(lantern_fish))

        
            







part1()