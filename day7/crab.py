#!/usr/bin/env python3

crabs = []

with open('input', 'r') as positions:
    parse = positions.read().split(',')
    crabs = [int(x) for x in parse]

print(str(crabs))

def fuel(crabs, target_position):
    cost = 0
    for pos in crabs:
        linear_cost = abs(pos - target_position)
        cost += int(linear_cost * (linear_cost + 1) / 2)
    return cost

costs = []
for target in range(min(crabs),max(crabs)+1):
    cost = fuel(crabs, target)
    print("cost to move all crabs to " + str(target) + " is " + str(cost))
    costs.append(cost)

print("minimal costs: " + str(min(costs)))
