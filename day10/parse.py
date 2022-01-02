#!/usr/bin/env python3

lines = []
with open('input', 'r') as data:
    lines = data.readlines()


def is_corrupted(line):
    open_bracket = [ '[', '(', '{', '<' ]
    close_bracket = [ ']', ')', '}', '>' ]

    score = { ")": 3, "]": 57, "}": 1197, ">": 25137 }
    bracket_stack = []

    for char in line:
        if char in open_bracket:
            bracket_stack.append(char)
        if char in close_bracket:
            # is it matching?
            if open_bracket.index(bracket_stack[-1]) == close_bracket.index(char):
                del bracket_stack[-1]
            else:
                #print("found mismatch at: " + char)
                #print("type: " + str(type(char)))
                return True, score[char]
    return False, 0

full_score = 0
incomplete = []
for line in lines:
    corrupted, score = is_corrupted(line)
    full_score += score
    if not corrupted:
        incomplete.append(line)
    #if corrupted:
    #    print("line is corrupted: " + line)
    #else:
    #    print("line is not corrupted: " + line)

print("score: ", str(full_score))

def incomplete_score(line):
    open_bracket = [ '[', '(', '{', '<' ]
    close_bracket = [ ']', ')', '}', '>' ]

    bracket_stack = []
    for char in line:
        if char in open_bracket:
            bracket_stack.append(char)
        if char in close_bracket:
            # is it matching?
            if open_bracket.index(bracket_stack[-1]) == close_bracket.index(char):
                del bracket_stack[-1]
    
    points = { "(": 1, "[": 2, "{": 3, "<": 4 }
    score = 0
    for bracket in reversed(bracket_stack):
        score *= 5
        score += points[bracket]
    return score

scores = []
for line in incomplete:
    scores.append(incomplete_score(line))

scores.sort()
print(str(scores))

print("middle score: ", str(scores[int((len(scores)-1)/2)]))
