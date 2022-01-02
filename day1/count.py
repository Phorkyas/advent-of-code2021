#!/usr/bin/env python3

measurements = []
with open('input', 'r') as data:
    measurements = data.read().splitlines()


bigger_count = 0
for num, elem in enumerate(measurements):
    if num > 0 and elem >= measurements[num-1]:
        print(str(elem))
        bigger_count += 1

print("count of measurements bigger than preceeding: " + str(bigger_count))



