#!/usr/bin/env python3

signal = []
with open('input', 'r') as f:
    data = f.readlines()
    for line in data:
        parse = line.split('|')
        signal.append([parse[0].split(), parse[1].split()])

print("Input")
print(str(signal))

def equal(pat1, pat2):
    if len(pat1) != len(pat2):
        return False
    for let in pat1:
        if let not in pat2:
            return False
    return True

in1 = ''

in2 = 'cefdb'

if equal(in1, in2):
    print("equal")
else:
    print("something broken")

def subtract(pat1, pat2):
    res = []
    for l in pat1:
        if l not in pat2:
            res.append(l)
    return res

def decode(pattern, number):
    digits = ['ab' for i in range(10)]
    # find '1'
    for p in pattern:
        if len(p) == 2:
            print("1 is: " + p)
            digits[1] = p
        # find '4'
        elif len(p) == 4:
            print("4 is: " + p)
            digits[4] = p
        # find '7'
        elif len(p) == 3:
            print("7 is: " + p)
            digits[7] = p
        # find '8'
        elif len(p) == 7:
            print("8 is: " + p)
            digits[8] = p
    # of the pattern with length five:
    #   * the one where the segments of the '1' are in, is the three 
    #   * the one where the letters of seg_bd are in is the '5', 
    #   * the other one must be '2'
    seg_bd = subtract(digits[4], digits[1])
    for p in pattern:
        if len(p) == 5:
            if digits[1][0] in p and digits[1][1] in p:
                print("found 3: " + str(p))
                digits[3] = p
            elif seg_bd[0] in p and seg_bd[1] in p:
                print("found 5: " + str(p))
                digits[5] = p
            else:
                print("found 2: " + str(p))
                digits[2] = p

    # of the pattern with length six:
    #   * the one which does not contain all segments of the '1' is '6'
    #   * the one containing all segments of the '4' is '9'
    #   * remaining one is '0'
    for p in pattern:
        if len(p) == 6:
            if digits[1][0] not in p or digits[1][1] not in p:
                print("found 6: " + str(p))
                digits[6] = p
            elif digits[4][0] in p and digits[4][1] in p and digits[4][2] in p and digits[4][3] in p:
                print("found 9: " + p)
                digits[9] = p
            else:
                print("found 0: " + p)
                digits[0] = p

    for i in range(len(digits)):
        print(str(i) + " maps to " + digits[i])

    res = "" 
    for n in number:
        print(n)
        hit = False
        for i in range(len(digits)):
            if equal(str(n), str(digits[i])):
                print("hit: " + str(i))
                res += str(i)
                hit = True
                break
        if not hit:
            print("found no match for: " + n);

    if len(res) != 4:
        print("someting went wrong!")
    return int(res)


added = 0
for out in signal:
    added += decode(out[0], out[1])
    print("current sum: " + str(added))

print("final sum: " + str(added))
