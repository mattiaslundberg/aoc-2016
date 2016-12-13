from collections import Counter
favorite = 1352


def is_floor(x, y):
    c = x*x + 3*x + 2*x*y + y + y*y + favorite
    b = "{0:b}".format(c)
    ones = Counter(b).get("1", 0)
    return ones % 2 != 0


dist = {(1, 1): 0}
queue = [(1, 1)]

while len(queue):
    current = queue.pop(0)
    for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        next = current[0] + i[0], current[1] + i[1]
        if next not in dist and not is_floor(*next):
            dist[next] = dist[current] + 1
            queue.append(next)

print(dist[(31, 39)])
