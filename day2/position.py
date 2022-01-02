#!/usr/bin/env python3

commands = []
with open('input', 'r') as data:
    commands = data.read().splitlines()

course = []
for elem in commands:
    res = elem.split()
    if len(res) != 2:
        print("failed to parse: " + elem)
        continue
    # there is always the command followed by a number
    course.append([res[0], int(res[1])])

# start position            
depth = 0
horizontal_pos = 0

for cmd in course:
    if cmd[0] == "forward":
        horizontal_pos += cmd[1]
    elif cmd[0] == "up":
        depth -= cmd[1]
    elif cmd[0] == "down":
        depth += cmd[1]
    else:
        print("Unknown command: " + cmd[0])

print("depth: " + str(depth))
print("horizontal pos: " + str(horizontal_pos))

print("muliplied: " + str(depth * horizontal_pos))

