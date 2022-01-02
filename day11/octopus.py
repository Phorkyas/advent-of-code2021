#!/usr/bin/env python3

octopus = []
with open('input', 'r') as data:
    lines = data.readlines()
    for line in lines:
        octopus.append([int(x) for x in line.strip()])

print(str(octopus))

def get_neighbors(pos, limit):
    neighbors = []
    for change_0 in range(-1,2):
        for change_1 in range(-1,2):
            new_0 = pos[0] + change_0
            new_1 = pos[1] + change_1
            if change_0 == 0 and change_1 == 0:
                continue
            if new_0 >= 0 and new_0 < limit[0] and new_1 >= 0 and new_1 < limit[1]:
                neighbors.append([new_0, new_1])
    #print("in: " + str(pos) + " " + str(limit))
    #print("out: " + str(neighbors))
    return neighbors

#print(str(get_neighbors([0,0],[3,3])))
#print(str(get_neighbors([1,1],[3,3])))
#print(str(get_neighbors([2,2],[3,3])))


def simulate_step(octopus):
    flashing = []
    flashed = []
    for y in range(len(octopus)):
        for x in range(len(octopus[y])):
            octopus[y][x] += 1
            if octopus[y][x] > 9:
                flashing.append([y,x])

    #display(octopus)
    print("flashing: " + str(flashing))
    count = 0
    while len(flashing) > 0:
        new_flashing = []
        for pos in flashing:
            if pos not in flashed:
                flashed.append(pos)
        for pos in flashing:
            for nb in get_neighbors(pos, [len(octopus),len(octopus[0])]):
                octopus[nb[0]][nb[1]] += 1
                if octopus[nb[0]][nb[1]] > 9 and nb not in flashed and nb not in new_flashing: 
                    #print("appending: " + str(nb))
                    new_flashing.append(nb)
        #print("flashed: " + str(flashed))
        #print("new: " + str(new_flashing))
        flashing = new_flashing
        count += 1
        if count > 1000:
            print("ooops")
            break
    
    count = 0
    for y in range(len(octopus)):
        for x in range(len(octopus[y])):
            if octopus[y][x] > 9:
                octopus[y][x] = 0
                count += 1
    print("flashed: " + str(count))
    return count


def display(octopus):
    for y in range(len(octopus)):
        for x in range(len(octopus[y])):
            if octopus[y][x] > 9:
                print("*", end="")
            else:
                print(str(octopus[y][x]), end="")
        print("")
    

def synchronized(octopus):
    for y in range(len(octopus)):
        for x in range(len(octopus[y])):
            if octopus[y][x] != 0:
                return False
    return True

flashes = 0
display(octopus)
for step in range(1000):
    print("step = ", str(step))
    flashes += simulate_step(octopus)
    if synchronized(octopus):
        print("were synchronized in step: " + str(step + 1))
        display(octopus)
        break
   # display(octopus)

print("number of flashes: " + str(flashes))
    
