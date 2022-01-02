#!/usr/bin/env python3

# Different representation, where we only save the counts of fish
# with certain days to breed
fish = [0 for i in range(9)]
with open('input', 'r') as data:
    parse = data.read().split(',')
    for x in parse:
        fish[int(x)] += 1

def simulate(fish):
    # make a real copy!
    old_fish = fish[:]
    # shift them all by one
    for i in range(len(fish) - 1):
        fish[i] = old_fish[i+1]

    # passing zero, they breed (with initial count of 8)
    fish[len(fish)-1] = old_fish[0]
    # and start again with six
    fish[6] += old_fish[0]

def count(fish):
    count = 0
    for i in range(len(fish)):
        count += fish[i]
    return count

def show(fish):
    for i in range(len(fish)):
        print(fish[i], end=" ")
    print("")

for days in range(256):
    #show(fish)
    simulate(fish)
    print("Day " + str(days) + " " + str(count(fish)))

print("How much is the fish? " + str(count(fish)))
    

