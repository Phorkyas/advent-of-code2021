#!/usr/bin/env python3

paper = [[False for x in range(655*2+1)] for y in range(447*2+1)]
with open('input', 'r') as dots:
    positions = dots.readlines()
    for pos in positions:
        x,y = pos.strip().split(',')
        paper[int(y)][int(x)] = True

def print_paper(paper):
    for y in range(len(paper)):
        for x in range(len(paper[0])):
            if paper[y][x]:
                print("#", end="")
            else:
                print(".", end="")
        print("")

#print_paper(paper)

def fold_at_y(y_fold, paper):
    # x range untouched, line that is folded is retained
    # will create some empty space...
    new_paper = [[False for x in range(len(paper[0]))] for y in range(y_fold)]

    for y in range(y_fold):
        for x in range(len(paper[0])):
            new_paper[y][x] = paper[y][x] or paper[2*y_fold-y][x]
    return new_paper

def fold_at_x(x_fold, paper):
    # y range untouched, x will be halved
    new_paper = [[False for x in range(x_fold)] for y in range(len(paper))]

    for y in range(len(paper)):
        for x in range(x_fold):
            new_paper[y][x] = paper[y][x] or paper[y][2*x_fold-x]
    return new_paper

def count_dots(paper):
    count = 0
    for y in range(len(paper)):
        for x in range(len(paper[0])):
            if paper[y][x]:
                count += 1
    return count

# now read the instructions
# and execute all of 'em
with open('instructions', 'r') as data:
    instructions = data.readlines()
    for instruction in instructions:
        cmd,number = instruction.strip().split('=')
        if cmd == "fold along x":
            paper = fold_at_x(int(number), paper)
        elif cmd == "fold along y":
            paper = fold_at_y(int(number), paper)
        else:
            print("unknown command: " + cmd)


print("folding done...")
print_paper(paper)

