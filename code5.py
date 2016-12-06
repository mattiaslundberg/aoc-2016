import hashlib

data = "ffykfhsq"
index = 0
result = ""

while True:
    hash = hashlib.md5(bytes("%s%s" % (data, index), "utf-8")).hexdigest()
    if hash.startswith("00000"):
        print(index, hash)
        result += hash[5]

        if len(result) >= 8:
            break

    index += 1
print(result)
