#!/usr/bin/env python3

output = []
with open('input', 'r') as f:
    data = f.readlines()
    for line in data:
        parse = line.split('|')
        output.append(parse[1].split())

#print(str(output))

unique = [2, 4, 3, 7]

count = 0
for out in output:
    for sig in out:
        if len(sig) in unique:
            count += 1

print("count: " + str(count))
