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

# part two: use them as bit filter

from collections import Counter

# test data
#oxygen = ['00100','11110','10110','10111','10101','01111','00111','11100','10000', '11001', '00010','01010']

oxygen = bin_data

for pos in range(len(oxygen)):
    # form a list of bits at pos
    bit_list = [x[pos] for x in oxygen]
    counts = Counter(bit_list).most_common(2)
    most_common_bit = counts[0][0]
    if len(counts) > 1 and counts[0][1] == counts[1][1]:
        print("bits count equal at pos: " + str(pos))
        most_common_bit = '1'
    print("most common bit is: " + most_common_bit)
    filtered = list(filter(lambda x: x[pos] == most_common_bit, oxygen))
    oxygen = filtered
    if len(oxygen) < 2:
        print("items remaining: " + str(len(oxygen)))
        print("oxygen: " + oxygen[0])
        print("oxygen: " + str(int(oxygen[0], 2)))
        break

#co2 = ['00100','11110','10110','10111','10101','01111','00111','11100','10000', '11001', '00010','01010']

co2 = bin_data

for pos in range(len(co2)):
    # form a list of bits at pos
    bit_list = [x[pos] for x in co2]
    counts = Counter(bit_list).most_common(2)
    least_common_bit = Counter(bit_list).most_common(2)[1][0]
    if counts[0][1] == counts[1][1]:
        print("bit counts equal at pos " + str(pos))
        least_common_bit = '0'
    print("least common bit is: " + least_common_bit)
    filtered = list(filter(lambda x: x[pos] == least_common_bit, co2))
    co2 = filtered
    if len(co2) < 2:
        print("items remaining: " + str(len(co2)))
        print("co2 scrubber: " + co2[0])
        print("co2: " + str(int(co2[0], 2)))
        break

print('life support rating: ' + str(int(oxygen[0], 2) * int(co2[0], 2))) 
