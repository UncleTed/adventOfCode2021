def part1():
    horizontal = 0
    depth = 0
    with open("./long.txt", "r") as f:
        for line in f: 
            cmd, amount = line.split()
            if (cmd == 'forward'):
                horizontal = horizontal + int(amount)
            elif (cmd == 'up'):
                depth = depth - int(amount)
            elif (cmd == 'down'):
                depth = depth + int(amount)

    print('h: ', horizontal, ' d: ', depth, 'total: ', depth * horizontal)



def part2():
    horizontal = 0
    depth = 0
    aim = 0
    with open("./long.txt", "r") as f:
        for line in f: 
            cmd, amount = line.split()
            if (cmd == 'forward'):
                horizontal = horizontal + int(amount)
                depth = depth + (aim * int(amount))
            elif (cmd == 'up'):
                aim = aim - int(amount)
            elif (cmd == 'down'):
                aim = aim + int(amount)

    print('h: ', horizontal, ' d: ', depth, 'total: ', depth * horizontal)
part1()
part2()
