import hashlib
data = "ngcjuoqr"
index = 0
found = 0


def hash(i):
    return hashlib.md5(bytes("%s%s" % (data, i), "utf-8")).hexdigest()


hashes = [hash(i) for i in range(1000000)]


def has_3(hash):
    for i in range(len(hash) - 2):
        c = hash[i]
        if hash[i] == hash[i + 1] == hash[i + 2]:
            return True, c
    return False, None


def has_5(char, index):
    for j in range(index + 1, index + 1001):
        hash = hashes[j]
        for i in range(len(hash) - 4):
            if char == hash[i] == hash[i + 1] == hash[i + 2] == hash[i + 3] == hash[i + 4]:
                return True
    return False



while found < 64:
    hash = hashes[index]
    h3, char = has_3(hash)
    if h3 and has_5(char, index):
        found += 1
        print("found", found, index)
    index += 1
