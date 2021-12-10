from dataclasses import dataclass

opened = [ '[', '{', '(', '<']
closed = [ ']', '}', ')', '>']

illegal = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}
@dataclass
class open_close:
    open_paren: str
    close_paren: str



def part1():    
    score = 0
    input_lines = []
    with open("./long.txt", "r") as f:
        for line in f:
            input_lines.append([l for l in line])
        for line in input_lines:
            stack = []
            for l in line:
                if l in opened:
                    stack.append(l)
                elif l in closed:
                    top = stack.pop()
                    open_index = opened.index(top)
                    if closed.index(l) != open_index:
                        score += illegal[l]
                        print(F'Expected {closed[open_index]} but got {l} scored: {illegal[l]}')
                        break

    print(score)

part1()