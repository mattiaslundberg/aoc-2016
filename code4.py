from collections import Counter
data = open("input4.txt")

result = 0
for line in data.readlines():
    parts = line.split("-")
    sectorid = parts[-1].split("[")[0]
    checksum = list(parts[-1].split("[")[1][:-2])
    chars = "".join(parts[:-1])

    counter = Counter(chars).most_common()

    def sorter(pair):
        value = pair[1]
        order = 1000 - ord(pair[0])
        key = float("{}.{}".format(value, order))
        return key

    counter.sort(key=sorter, reverse=True)

    for char, count in counter[:5]:
        expected = checksum.pop(0)
        if expected != char:
            break
    else:
        result += int(sectorid)


print(result)
