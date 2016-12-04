data = open("input3.txt")

possible = 0

for line in data.readlines():
    sides = map(int, line.split())
    sides = sorted(sides)

    if sides[0] + sides[1] > sides[2]:
        possible += 1
print(possible)
