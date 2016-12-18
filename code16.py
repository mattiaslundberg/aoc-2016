data = "11011110011011101"
target = 272

while len(data) < target:
    a = data[:]
    b = data[::-1].replace("0", "_").replace("1", "0").replace("_", "1")
    data = "%s0%s" % (a, b)

data = data[:target]

while len(data) % 2 == 0:
    next = ""
    for i in range(0, len(data) - 1, 2):
        if data[i] == data[i + 1]:
            next += "1"
        else:
            next += "0"
    data = next

print("checksum", data)
