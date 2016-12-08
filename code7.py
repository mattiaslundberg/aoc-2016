import re
data = open("input7.txt")

result = 0


def has_abba(s):
    for i in range(len(s) - 3):
        if s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1]:
            return True
    return False


for address in data.readlines():
    inside = re.findall(r"\[(\w+)\]", address)
    outside = re.findall(r"^(\w+)\[", address) + re.findall(r"\](\w+)\[", address) + re.findall(r"\](\w+)$", address)

    inside_has_abba = list(map(has_abba, inside))
    outside_has_abba = list(map(has_abba, outside))

    if any(outside_has_abba) and not any(inside_has_abba):
        result += 1

print(result)
