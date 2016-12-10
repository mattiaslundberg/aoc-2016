import re
data = open("input10.txt")


bots = [
    {"chips": [], "give_low": None, "give_high": None}
    for i in range(300)
]


def move_chips(initial_bot):
    remaining = [initial_bot]
    while len(remaining):
        b = remaining.pop()
        high, low = b["give_high"], b["give_low"]

        if 61 in b["chips"] and 17 in b["chips"]:
            print("responible", bots.index(b))

        if len(b["chips"]) >= 2 and low is not None and low is not None:
            high, low = bots[high], bots[low]
            remaining += [high, low]
            low["chips"].append(min(*b["chips"]))
            high["chips"].append(max(*b["chips"]))
            b["chips"] = []


for action in data.readlines():
    if action.startswith("value"):
        value, bot = map(int, re.findall(r"\d+", action))
        bots[bot]["chips"].append(value)
    elif action.startswith("bot"):
        bot, low, high = map(int, re.findall(r"\d+", action))
        bots[bot]["give_low"] = low
        bots[bot]["give_high"] = high

    move_chips(bots[bot])
