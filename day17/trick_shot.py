#!/usr/bin/env python3

def has_hit(pos, area):
    x = pos[0]
    y = pos[1]

    if x >= area[0][0] and x <= area[0][1]:
        if y >= area[1][0] and y <= area[1][1]:
            return True
    return False

def do_step(position, velocity):
    position[0] += velocity[0]
    position[1] += velocity[1]

    if velocity[0] > 0:
        velocity[0] -= 1
    elif velocity[0] < 0:
        velocity[0] += 1

    velocity[1] -= 1

    return position, velocity

# test area
#area = [[20, 30], [-10,-5]]

area = [[96, 125], [-144,-98]]

solution = [0, [0,0]]
count = 0
for v_x in range(0, 200):
    for v_y in range(-400, 400):
        position = [0, 0]
        velocity = [v_x, v_y]

        max_y = 0
        for i in range(400):
            position, velocity = do_step(position, velocity)
            max_y = max(max_y, position[1])
            if has_hit(position, area):
                count += 1
                if max_y > solution[0]:
                    solution = [max_y, [v_x, v_y]]
                break

print(str(solution))
print(str(count))
