from collections import Counter
data = open("input6.txt")

lines = data.readlines()

columns = ["", "", "", "", "", "", "", ""]

for line in lines:
    line = line.strip()

    for i in range(8):
        columns[i] += line[i]
print(columns)

for column in columns:
    c = Counter(column)
    print(c.most_common(1)[0][0])
