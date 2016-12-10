data = open("input9.txt").read().strip()
index = 0
blocked_until_index = -1

while len(data) > index:
    if data[index] == "(" and index >= blocked_until_index:
        last = index
        while data[last] != ")":
            last += 1
        chars, times = map(int, data[index + 1:last].split("x"))
        to_copy = data[last + 1:last + 1 + chars]
        inserted = str(to_copy * (times - 1))
        data = data[:index] + inserted + data[last + 1:]
        blocked_until_index = index + len(inserted) + len(to_copy)

    index += 1

print(len(data))
