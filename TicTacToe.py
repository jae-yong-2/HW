import random

x, y, turn = 0, 0, 0
BLANK = ' '
board = [[BLANK, BLANK, BLANK],
         [BLANK, BLANK, BLANK],
         [BLANK, BLANK, BLANK], ]


def write(player, write):
    while (True):
        print(f"PLAYER {player}'s turn(x y)");
        x, y = input("input x y : ").split()
        x = int(x)
        y = int(y)
        if x > 2 or y > 2:
            print("retry");
            continue
        if board[x][y] == BLANK:
            board[x][y] = write
            break
        else:
            print("Wrong Position !!\n");
            continue


def game():
    print("1.person vs person 2.person vs computer\n select 1 or 2")
    s = int(input())

    if s == 1:
        while (True):
            print("x|y [0]|[1]|[2]")
            for a in range(3):
                b = 0
                print("    ---|---|---")
                print(f'[{a}] {board[a][b]}  | {board[a][b + 1]} | {board[a][b + 2]} ');
            print("    ---|---|---")

            print(f'turn {turn}')
            if turn % 2 == 1:
                write(2, 'X')
            else:
                write(1, 'O')


game()
