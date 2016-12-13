data = list(map(lambda s: s.strip(), open("input12.txt").readlines()))

registers = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
}
current = 0

def get_or_int(value):
    r = registers.get(value)
    if r is None:
        r = int(value)
    return r

while current < len(data):
    instr = data[current]
    action = instr.split(" ")[0]
    if action == "cpy":
        _, f, t = instr.split(" ")
        new_value = get_or_int(f)
        registers[t] = new_value
    elif action == "inc":
        var = instr.split(" ")[1]
        registers[var] += 1
    elif action == "dec":
        var = instr.split(" ")[1]
        registers[var] -= 1
    elif action == "jnz":
        _, var, dist = instr.split(" ")
        if get_or_int(var) != 0:
            current += int(dist)
            continue
    current += 1

print(registers)
