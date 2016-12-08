from itertools import chain
data = open("input8.txt")

# display[row][col]
display = [[False for _ in range(50)] for _ in range(6)]

for instr in data.readlines():
    action = instr.split(" ")[0]

    if action == "rect":
        col, row = map(int, instr.split(" ")[1].split("x"))
        for r in range(row):
            for c in range(col):
                display[r][c] = True

    elif "row" in instr:
        row, cols = map(int, instr.split("y=")[1].split(" by "))
        for _ in range(cols):
            temp = display[row][-1]
            for c in range(48, -1, -1):
                display[row][c+1] = display[row][c]
            display[row][0] = temp

    elif "column" in instr:
        col, rows = map(int, instr.split("x=")[1].split(" by "))
        col = col % 50
        rows = rows % 6
        for _ in range(rows):
            temp = display[-1][col]
            for r in range(4, -1, -1):
                display[r+1][col] = display[r][col]
            display[0][col] = temp

    else:
        print("failed to handle", instr)
        break


print(sum(chain.from_iterable(display)))
