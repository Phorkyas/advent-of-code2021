#!/usr/bin/env python3

fish = []
with open('input', 'r') as data:
    parse = data.read().split(',')
    fish = [int(x) for x in parse]

def simulate(fish):
    new_fish = []
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            new_fish.append(8)
        else:
            fish[i] -= 1
    for f in new_fish:
        fish.append(f)

def counts(fish):
    for i in range(9):
        count = 0
        for f in fish:
            if f == i:
                count += 1
        print(count, end=" ")
    print("")

for days in range(80):
    #counts(fish)
    #print(str(fish))
    simulate(fish)
    print("Day " + str(days) + " " + str(len(fish)))

print("How much is the fish? " + str(len(fish)))
    

