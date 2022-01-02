#!/usr/bin/env python3

measurements = []
with open('input', 'r') as data:
    measurements = data.read().splitlines()


three_sums = []
for i in range(len(measurements)):
    if i + 3 < len(measurements):
        three_sums.append(int(measurements[i]) + int(measurements[i+1]) + int(measurements[i+2]))

print(three_sums[0])
print(three_sums[1])

print("number of three sums" + str(len(three_sums)))
larger_count = 0
for i in range(len(three_sums)):
    if i + 1 < len(three_sums):
        if three_sums[i+1] > three_sums[i]:
            larger_count += 1

print("count of measurements bigger than preceeding: " + str(larger_count))



