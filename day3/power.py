#!/usr/bin/env python3

bin_data = []
with open('input', 'r') as data:
    bin_data = data.read().splitlines()

wideness = len(bin_data[0])
print(str(wideness) + " wide binary numbers")


# gamma rate is most common bit in each position
# epsilon is the least common bit

gamma = ''
epsilon = ''
for pos in range(wideness):
    zero_count = 0
    one_count = 0
    for num in bin_data:
        if num[pos] == '0':
            zero_count += 1
        elif num[pos] == '1':
            one_count +=1
        else:
            print("boom - something wrong at: " + pos)

    if zero_count > one_count:
        gamma += '0'
        epsilon += '1'
    elif one_count > zero_count:
        gamma += '1'
        epsilon += '0'
    else:
        print("uhuhu - dunno what to do")

print('gamma: ' + gamma)
print('epsilon: ' + epsilon)

print('converted: ' + str(int(gamma, 2)))

print('power: ' + str(int(gamma, 2) * int(epsilon, 2)))
