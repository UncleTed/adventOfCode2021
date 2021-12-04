from collections import Counter


def part1():
    gamma_rate = ''
    episilon_rate = ''
    bits = []
    with open("./short.txt", "r") as f:
        lines = [list(line.rstrip()) for line in f]
    length = len(lines[0])
    for i in range(length):
        bits.append(''.join(list(map(lambda l: l[i], lines))))

    for i in range(len(bits)):
        gamma_rate += Counter(bits[i]).most_common()[0][0]
        episilon_rate += Counter(bits[i]).most_common()[1][0]
        
    
    print('\u03B3' ,' * ' ,'\u03B5', ' = ', int(gamma_rate,2) * int(episilon_rate,2))     
 

def most_common_bit(bit_position, the_lines):
    mc = Counter((list(map(lambda l: l[bit_position], the_lines)))).most_common()
    if(len(mc) == 1):
        return mc[0][0]
    if (mc[0][1] == mc[1][1]):
        return '1'
    return mc[0][0]

def least_common_bit(bit_position, the_lines):
    mc = Counter((list(map(lambda l: l[bit_position], the_lines)))).most_common()
    if(len(mc) == 1):
        return mc[0][0]
    if(mc[0][1] == mc[1][1]):
        return '0'
    return mc[1][0]

def part2():
    o2_generator = ''
    co2_scrubber = ''
    bits =[]
    with open("./long.txt", "r") as f:
        lines = [line.rstrip() for line in f]

    length = len(lines[0])
    
    o2_generator = co2_scrubber = lines
    for i in range(length):
        most_common = most_common_bit(i, o2_generator)
        o2_generator = list(filter(lambda l: l[i] == most_common, o2_generator))
        least_common = least_common_bit(i, co2_scrubber)
        co2_scrubber = list(filter(lambda l: l[i] == least_common, co2_scrubber))
    print(''.join(o2_generator))
    print(co2_scrubber)
    # 
    # 4175451 is too high
    print('o2 * co2 = ' ,int(''.join(o2_generator),2) * int(''.join(co2_scrubber),2))


part1()
part2()