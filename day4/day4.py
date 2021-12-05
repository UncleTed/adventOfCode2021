def print_board(board):
    print('-------')
    for b in board:
        print(b)


def mark_number(board, number):
    for row in board:
        for b in row:
            if ( b[0] == number):
                b[1] = True

def bingo(board):
    if (len(board) > 0):
        for row in board:
            all_true = [b for b in row if b[1] == True]
            if (len(all_true) == len(row)):
                return True

        cols = len(board)
        rows = len(board)
        r = 0
        c = 0
        for c in range(5):
            count_of_true = 0
            for r in range(5):
                if(board[r][c] == True):
                    count_of_true += 1
            if (count_of_true == 5):
                return True
        return False  
                


def sum_unmarked(board):
    sum = 0
    for row in board:
        for r in row:
            if(r[1] == False):
                sum += int(r[0])
    return sum

def part1():
    boards = []
    with open("long.txt") as f:
        draw_number = iter(f.readline().split(','))
        b = []
        for line in f:
            if(not line.isspace()):
                line.rstrip('\n')
                b.append([[l,False] for l in line.split() if not l.isspace()])
            else:
                # print_board(b)
                boards.append(b)
                b = []

    go = True
    while (go):
        try:
            num = next(draw_number)
            print('drawing number: ', num)
            for b in boards:
                # print(b)
                mark_number(b, num)

            for b in boards:
                if(bingo(b)):
                    print("Bingo!")
                    print_board(b)
                    print(sum_unmarked(b))
                    print(num)
                    print('answer: ' , sum_unmarked(b) * int(num))
                    go = False
                    break


        except StopIteration:
            go = False
    # for b in boards:
    #     print_board(b)

# 27475 is too low
part1()