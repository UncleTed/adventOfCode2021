def part1():
    digits = {0: 6, 1: 2 ,2: 5, 3: 5, 4: 4, 5: 5, 6:6, 7: 3, 8: 7, 9: 6}
    input_lines = []
    with open("./long.txt", "r") as f:
        for line in f:
            input_lines.append(line.strip().split(' | ')[1].split(' '))


    count = 0
    for line in input_lines:
        for display in line:
            print(display)
            if (len(display) == 2 or len(display) == 4 or len(display) == 3 or len(display) == 7):
                count += 1

    print(count)
if __name__ == '__main__':
    part1()
    