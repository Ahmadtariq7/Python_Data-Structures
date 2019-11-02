class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size


def _get_hash(self, key):
    # Check if it is int, string, tuple
    if type(key) == int:
        return key % self.size
    elif type(key) == str:  # Taking Mod of total length of string..
        length = len(key)
        return length % self.size
    elif type(key) == tuple:
        length = len(key)
        return length % self.size


HashMap._get_hash = _get_hash


def add(self, key, value):
    key_hash = self._get_hash(key)
    key_value = [key, value]

    # Insert or update: "upsert"
    self.map[key_hash] = [key_value]  # Notice the Double List.
    return True


HashMap.add = add


def get(self, key):
    key_hash = self._get_hash(key)
    if self.map[key_hash] is not None:
        for pair in self.map[key_hash]:
            if pair[0] == key:
                return pair[1]
    raise KeyError(str(key))


HashMap.get = get


def __str__(self):
    ret = ""
    for i, item in enumerate(self.map):  # ENUMERATE FOR THE INDEX LOCATION FINDING..
        if item is not None:
            ret += str(i) + ": " + str(item) + "\n"
    return ret


HashMap.__str__ = __str__

print(":::::::::: FOR AVOIDING HASH COLLISION :::::::::::::::")


def add(self, key, value):
    key_hash = self._get_hash(key)
    key_value = [key, value]

    if self.map[key_hash] is None:
        self.map[key_hash] = [key_value]
        return True
    else:
        # Check if its an update
        for pair in self.map[key_hash]:
            if pair[0] == key:
                print("Updating: ", key)
                pair[1] = value
                return True
        # Nope, it's a collision, insert it
        self.map[key_hash].append(key_value)
        return True


HashMap.add = add


def delete(self, key):
    key_hash = self._get_hash(key)
    if self.map[key_hash] is None:
        raise KeyError(str(key))
    for i in range(0, len(self.map[key_hash])):
        if self.map[key_hash][i][0] == key:
            self.map[key_hash].pop(i)
            return True


HashMap.delete = delete

h = HashMap()
h.add(17, "Seventeen")
h.add(26, "TwentySix")
h.add(35, "ThirtyFive")
h.add(25, "TwentyFive")

print(h)
print(h.get(26))
print(h.get(25))
h.delete(17)
print(h)