class HashTable:
    """
    """

    # the slots list holds keys which map to the associated data in the data list
    # the initial size is set to a prime number for maximum efficiency of the
    # collision resolution algorithm
    def __init__(self):
        self.size = 67
        self.slots = [None] * self.size
        self.data = [None] * self.size

    # IMPORTANT this implementation replaces values that have the same key
    def put(self, key, data):
        hash_val = self.hash_func(key, self.size)

        if self.slots[hash_val] == None: #target empty
            self.slots[hash_val] = key
            self.data[hash_val] = data
        else:
            if self.slots[hash_val] == key: #target holds the same key
                self.data[hash_val] = data #replaces same key data
            else:
                # linear probing
                next_slot = self.rehash_func(hash_val, self.size)
                # cycle until an empty or same key slot is found
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash_func(next_slot, self.size)

            if self.slots[next_slot] == None:
                self.slots[next_slot] = key
                self.data[next_slot] = data
            else:
                self.data[next_slot] = data #replaces same key data

    def get(self, key):
        start_slot = self.hash_func(key, self.size)

        data = None
        stop = False
        found = False
        pos = start_slot

        # cycle until the key is found, an empty slot is encountered or the whole key list is traversed
        while self.slots[pos] != None and not found and not stop:
            if self.slots[pos] == key:
                data = self.data[pos]
                found = True
            else:
                pos = self.rehash_func(pos, self.size)
                if pos == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    # implements the remainder method
    def hash_func(self, key, size):
        return key % size

    # implements linear probing method for open addressing collision resolution
    def rehash_func(self, old_hash, size):
        return (old_hash + 1) % size

    def len(self):
        return self.size
