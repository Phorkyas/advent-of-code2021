#!/usr/bin/env python3

level = []

with open('input', 'r') as lines:
    parse = lines.readlines()
    for line in parse:
        level.append([int(char) for char in line.strip()])

def is_lowest(x, y, level):
    # with python lists x and y are swapped.... dang
    height = len(level)
    length = len(level[y])
    if x+1 < length:
        if level[y][x] >= level[y][x+1]:
            return False
    if y+1 < height:
        if level[y][x] >= level[y+1][x]:
            return False
    if x-1 >= 0:
        if level[y][x] >= level[y][x-1]:
            return False
    if y-1 >= 0:
        if level[y][x] >= level[y-1][x]:
            return False
    return True

for y in range(len(level)):
    for x in range(len(level[y])):
        print(str(level[y][x]), end="")
    print("")

risk = 0
lowest_positions = []
for y in range(len(level)):
    for x in range(len(level[y])):
        if is_lowest(x,y, level):
            lowest_positions.append([x,y])
            risk += level[y][x] + 1

print("Risk level: " + str(risk))
print("low pos: " + str(lowest_positions))

def get_neighbors(position, level):
    # with python lists x and y are swapped.... dang
    x = position[0]
    y = position[1]
    height = len(level)
    length = len(level[y])
    res = []
    if x+1 < length:
        if level[y][x+1] < 9:
            res.append([x+1,y])
    if y+1 < height:
        if level[y+1][x] < 9:
            res.append([x,y+1])
    if x-1 >= 0:
        if level[y][x-1] < 9:
            res.append([x-1,y])
    if y-1 >= 0:
        if level[y-1][x] < 9:
            res.append([x,y-1])
    return res

def print_basin(basin, level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            if [x,y] in basin:
                print(str(level[y][x]), end="")
            else:
                print(".", end="")
        print("")

def mark_basin(position, level):
    basin = []
    basin.append(position)

    to_visit = get_neighbors(position, level)

    count = 0
    while len(to_visit) > 0:
        new = []
        for p in to_visit:
            if p not in basin:
                basin.append(p)
        for p in to_visit:
            for l in get_neighbors(p, level):
                if l not in basin:
                    new.append(l)
        to_visit = new[:]
        count += 1
        if count > 10000:
            print("ooops")
            break
    print_basin(basin, level)
    return len(basin)

basin_sizes = []
for pos in lowest_positions:
    size = mark_basin(pos, level)
    print("mark basin for: " + str(pos) + " size: " + str(size))
    basin_sizes.append(size)

basin_sizes.sort(reverse=True)

print("largest basin: ", str(basin_sizes[0]))
print("second largest basin: ", str(basin_sizes[1]))
print("third largest basin: ", str(basin_sizes[2]))
print("result: " + str(basin_sizes[0] * basin_sizes[1] * basin_sizes[2]))

