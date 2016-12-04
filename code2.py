data = open("input2.txt")

for line in data.readlines():
    pos = 5
    for action in line:
        if action == "U" and pos > 3:
            pos -= 3
        elif action == "D" and pos < 7:
            pos += 3
        elif action == "L" and pos in [2, 3, 5, 6, 8, 9]:
            pos -= 1
        elif action == "R" and pos in [1, 2, 4, 5, 7, 8]:
            pos += 1
    print(pos)
