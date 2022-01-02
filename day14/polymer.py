#!/usr/bin/env python3

pair_grow = {}
with open('rules', 'r') as infile:
    rules = infile.readlines()
    for rule in rules:
        pair = rule.split(' -> ')
        # each pair generates two new pairs with the letter in between
        pair_grow[pair[0]] = [pair[0][0]+pair[1].strip(), pair[1].strip()+pair[0][1]]


print(str(pair_grow))

def add_or_incr(keymap, key, value):
    if key not in keymap.keys():
        keymap[key] = value
    else:
        keymap[key] += value

def convert_polymer(polymer):
    pair_count = {}
    for i in range(len(polymer)-1):
        pair = polymer[i:i+2]
        # meh, shouldn't that go easier?
        add_or_incr(pair_count, pair, 1)
 
    return pair_count

# for test data
#template = "NNCB"

# real input
template = "ONHOOSCKBSVHBNKFKSBK"

polymer = convert_polymer(template)
print(str(polymer))

def grow_polymer(polymer, rule):
    # a polymer is now only the count of the pairs
    # - as I was impatient and had no clue I looked at reddit for ideas - this was the only time though 
    increment = {}
    for pair in polymer.keys():
        if pair in rule.keys():
            # the old pair is broken, so we need to deduct the count
            add_or_incr(increment, pair, -polymer[pair])
            # two new pairs are produced though
            produced = rule[pair]
            for p in produced:
                add_or_incr(increment, p, polymer[pair])

    for pair in increment.keys():
        add_or_incr(polymer, pair, increment[pair])
    
    return polymer

def count(polymer):
    # All letters in the chain are counted twice *except* the start and end which are only counted once.
    # Thus we initialize the count list with "1" for these two letters.
    # Then we can just count all letters in the pairs and finally divide by two. 
    
    # for test data, compare teh templates
    #counts = {"N":1, "B":1}
    
    # for the real data
    counts = {"O":1, "K":1}
    for c in polymer.keys():
        add_or_incr(counts, c[0], polymer[c])
        add_or_incr(counts, c[1], polymer[c])
    res = []
    for count in counts.values():
        res.append(int(count / 2))
    return list(sorted(res))

for steps in range(40):
    polymer = grow_polymer(polymer, pair_grow)

counts = count(polymer)
print(str(counts))

common_vs_leastcommon = counts[-1] - counts[0]
print("result: " + str(common_vs_leastcommon))
