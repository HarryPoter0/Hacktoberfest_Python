data = [
    ("Mango", "Hafus, Kesar, Langdo"),
    ("Banana", "Green, Yellow"),
    ("Orange", "Narangi, Mosambi"),
]


def simple_hash(s: str) -> int:
    """Simple hash"""
    basic_hash = ord(s[0])
    return basic_hash % 10


def get(k: str) -> str:
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


keys = [""] * 10
values = keys.copy()

for key, value in data:
    h = simple_hash(key)
    print(key, h)
    keys[h] = key
    values[h] = value
print(keys)
print(values)
print()
print(get("Lemo"))



