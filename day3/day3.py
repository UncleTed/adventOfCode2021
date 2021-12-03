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
        
    
    print('gamma: ', int(gamma_rate,2))     
    print('episilon: ', int(episilon_rate,2))  


    


part1()