data = map(lambda d: d.strip(), open("input1.txt").read().split(","))

direction = 0
position_x, position_y = 0, 0
for move in data:
    rotation = move[:1]
    distance = int(move[1:])

    if rotation == "R":
        direction = direction + 1 if direction < 3 else 0
    elif rotation == "L":
        direction = direction - 1 if direction > 0 else 3

    if direction == 0:
        position_y += distance
    if direction == 2:
        position_y -= distance

    if direction == 1:
        position_x += distance
    if direction == 3:
        position_x -= distance

print(abs(position_x) + abs(position_y))
