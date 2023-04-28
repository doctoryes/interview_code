
## Hashtables: Arguably the single most important data structure known to womankind.
# You should know how they work. Be able to implement one using only arrays in your
# favorite language, in about the space of one interview.

import hashlib

HASH_BITS_TO_USE = 12
HASH_ARR_LEN = 2 ** HASH_BITS_TO_USE

class HashMap:
    def __init__(self):
        self.hash_arr = [[] for __ in range(0, HASH_ARR_LEN)]
        self.items = 0

    def _compute_hash_index(self, key):
        """
        Hash the key, returning an index into the array.
        """
        if isinstance(key, str):
            key = key.encode('utf8')

        # Compute the MD5 sum of the key.
        h = hashlib.md5(key).digest()

        # Use only the last HASH_BITS_TO_USE of the sum, using bit manipulation.
        # Handles HASH_BITS_TO_USE between 1 and 32 only.
        hash_index = 0
        for byte_num in range(1, 4):
            hash_index += h[-byte_num] & (HASH_ARR_LEN - 1) >> ((byte_num - 1) * 8)

        return hash_index

    def __setitem__(self, key, value):
        h = self._compute_hash_index(key)
        exists = False
        for idx, (k, v) in enumerate(self.hash_arr[h]):
            if k == key:
                # Key already exists so update the value.
                self.hash_arr[h][idx] = (k, value)
                exists = True
                break
        if not exists:
            self.hash_arr[h].append((key, value))

    def __getitem__(self, key):
        """
        Return the value for the key. Raises KeyError if key doesn't exist.
        """
        h = self._compute_hash_index(key)
        value = None
        for k, v in self.hash_arr[h]:
            if k == key:
                value = v
                break
        if value is None:
            raise KeyError(key)
        return value

    def __str__(self):
        pairs = []
        for h in range(0, HASH_ARR_LEN):
            for k, v in self.hash_arr[h]:
                pairs.append(f"{repr(k)}: {repr(v)}")
        return "{" + ", ".join(pairs) + "}"



