import random
from enum import Enum


class Piece(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4
    EMPTY = 0


def create_table(n, m):
    table = []
    for i in range(n):
        table.append([])
        for _ in range(m):
            table[i].append(Piece.EMPTY)
    return table


def print_table(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            print(table[i][j].value, end=" ")
        print()


def fall_motion(table, i, j):
    if not table[i][j] == Piece.EMPTY:
        return None
    
    if i == 0 and table[i][j] == Piece.EMPTY:
        next_val = random.randrange(1, 5)
        if next_val == table[i + 1][j].value: 
            next_val -= 1
        if j > 0:
            if table[i][j - 1] == next_val:
                next_val -= 1
        if j < len(table[0]) - 1:
            if table[i][j + 1] == next_val:
                next_val -= 1
        if next_val == Piece.RED.value:
            table[i][j] = Piece.RED
        elif next_val == Piece.YELLOW.value:
            table[i][j] = Piece.YELLOW
        elif next_val == Piece.GREEN.value:
            table[i][j] = Piece.GREEN
        elif next_val == Piece.BLUE.value:
            table[i][j] = Piece.BLUE
        return None
    elif i == 0:
        return None
    elif table[i][j] == Piece.EMPTY:
        if table[i - 1][j] == Piece.EMPTY:
            fall_motion(table, i - 1, j)
        table[i][j] = table[i - 1][j]
        table[i - 1][j] = Piece.EMPTY
        fall_motion(table, i - 1, j)
        return None


def refill_table(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == Piece.EMPTY:
                fall_motion(table, i, j)


def main():
    table = create_table(10, 10)
    refill_table(table)
    print_table(table)



if __name__ == "__main__":
    main()