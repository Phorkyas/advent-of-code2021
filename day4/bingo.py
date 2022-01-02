#!/usr/bin/env python3

numbers = []
with open('numbers', 'r') as data:
    numbers = data.read().split(',')


boards = []
with open('boards', 'r') as data:
    stuff = data.read()
    boardsplit = stuff.split("\n\n")
    for board in boardsplit:
        intboard = []
        lines = board.split("\n")
        if len(lines) != 5:
            continue
        for line in lines:
            intboard.append([int(n) for n in line.split()])
        boards.append(intboard)

print("parsed " + str(len(boards)) + " boards")

def mark_number(number, board, count):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[x][y] == number:
                #print("Zahl da in: " + str(x) + " " + str(y) + " - brett: " + str(count))
                board[x][y] += 100


def hat_bingo(zahlen):
    for zahl in zahlen:
        if zahl < 100:
            return False
    return True

def score(board):
    res = 0
    for y in range(len(board)):
        for el in board[y]:
            # sum all unmarked elements
            if el < 100:
                res += el
    return res

def gewonnen(board, number):
    for y in range(len(board)):
        spalte = [board[x][y] for x in range(len(board[0]))]
        if hat_bingo(spalte):
            real_col = [n - 100 for n in spalte]
            print("bingo in spalte: " + str(real_col))
            print("score: " + str(score(board)))
            print("result: " + str(number * score(board)))
            return True
    for zeile in board:
        if hat_bingo(zeile):
            print(str(board))
            real_row = [n - 100 for n in zeile]
            print("bingo in zeile: " + str(real_row))
            print("score: " + str(score(board)))
            print("result: " + str(number * score(board)))
            return True
    return False

winner_boards = []

for num in numbers:
    print("Markiere Zahl: " + num + " in Brett")
    count = 0
    for board in boards:
        count += 1
        mark_number(int(num), board, count)
        if count not in winner_boards and gewonnen(board, int(num)):
            print("BINGO!!")
            print("Board " + str(count) + " hat gewonnen")
            winner_boards.append(count)

print("finished - there where: " + str(len(winner_boards)) + " winner boards")
