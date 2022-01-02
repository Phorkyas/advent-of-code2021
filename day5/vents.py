#!/usr/bin/env python3

grid_size = 1000
draw_lines = []
with open('input', 'r') as data:
    lines = data.read().splitlines()
    for line in lines:
        parse = line.split()
        start = parse[0].split(',')
        end = parse[2].split(',')
        draw_lines.append([[int(start[0]), int(start[1])], [int(end[0]), int(end[1])]])

print(str(draw_lines))

def display(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[x][y] == 0:
                print(". ", end='')
            else:
                print(str(grid[x][y]) + " ", end='')
        print("")


grid = [[0 for x in range(grid_size)] for y in range(grid_size)]

display(grid)

def draw_line(coord, grid):
    if coord[0][0] == coord[1][0]:
        # vertical line
        x = coord[0][0]
        y_range = [coord[0][1], coord[1][1]]
        for y in range(min(y_range), max(y_range) + 1):
            grid[x][y] += 1
    elif coord[0][1] == coord[1][1]:
        # horizonal line
        y = coord[0][1]
        x_range = [coord[0][0], coord[1][0]]
        for x in range(min(x_range), max(x_range) + 1):
            grid[x][y] += 1
    elif abs(coord[0][1] - coord[1][1]) == abs(coord[0][0] - coord[1][0]):
        # diagonal 45 degrees
        y_step = int((coord[1][1]-coord[0][1]) / abs(coord[0][1]-coord[1][1]))
        x_step = int((coord[1][0]-coord[0][0]) / abs(coord[0][0]-coord[1][0]))
        y = coord[0][1]
        for x in range(coord[0][0], coord[1][0] + x_step, x_step):
            grid[x][y] += 1
            y += y_step
    else:
        print("something went wrong with line: " + str(coord))

for line in draw_lines:
    draw_line(line, grid)

print("after")

display(grid)

def score(grid):
    res = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[x][y] > 1:
                res += 1
    return res

print("total score: " + str(score(grid)))

