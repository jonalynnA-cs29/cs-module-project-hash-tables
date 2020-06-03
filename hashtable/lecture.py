# data = [None, None, None, None, None, None, None, None] # 8 Slots
class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'HashTableEntry({repr(self.key)},{repr(self.value)})'


data = [None] * 20

# Takes our string and turns it into a number


def my_hashing_function(s):
    string_bytes = s.encode()

    total = 0

    for b in string_bytes:
        # print(ord(c))
        total += b
    return total

# Takes our number and puts it into an array


def get_slot(s):
    hash_val = my_hashing_function(s)
    return hash_val % len(data)


def get(key):
    slot = get_slot(key)
    hash_entry = data[slot]

    if hash_entry is not None:
        return hash_entry.value
    return None


def put(key, value):
    slot = get_slot(key)
    data[slot] = HashTableEntry(key, value)


def delete(key):
    put(key, None)


put("beej", 3490)
put("foo", 999)
put("baz", 111)
print(data)

# print(data)
print(get("beej"))
# print(get("foo"))
print(get("bar"))
