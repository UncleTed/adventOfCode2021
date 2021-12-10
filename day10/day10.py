import statistics

open_to_close = {
    '[' : ']',
    '{' : '}', 
    '(': ')', 
    '<' : '>'
}
incomplete_scores = []

close_to_open = {
    ']' : '[',
    '}' : '{', 
    ')' : '(', 
    '>' : '<'
}

illegal = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}
incomplete = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
}

def score_incomplete(stack):
    score = 0
    for s in stack:
        score = (score*5)+incomplete[open_to_close[s]]
        
    # print(F'{stack} {score}')
    if score > 0:
        incomplete_scores.append(score)
         

def part1():    
    illegal_score = 0
    input_lines = []
    with open("./long.txt", "r") as f:
        for line in f:
            input_lines.append([l for l in line])
        for line in input_lines:
            stack = []
            for l in line:
                if l in open_to_close.keys():
                    stack.append(l)
                elif l in close_to_open.keys():
                    top = stack.pop()
                    
                    if close_to_open[l] != top:
                        illegal_score += illegal[l]
                        # print(F'Expected {open_to_close[top]} but got {l} scored: {illegal[l]}')
                        stack = []
                        break
            stack.reverse()
            score_incomplete(stack)

    print(F'Illegal score : {illegal_score}')
    # print(sorted(incomplete_scores))
    print(F'Incomplete score: {statistics.median(incomplete_scores)}')

part1()