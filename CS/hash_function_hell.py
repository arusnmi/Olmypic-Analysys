
class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key):
        # Simple hash function for strings
        return sum(ord(char) for char in str(key)) % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def put(self, key, value):
        hash_value = self.hash_function(key)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value  # Replace value if key already exists
            else:
                next_slot = self.rehash(hash_value)
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot)

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = value
                else:
                    self.data[next_slot] = value  # Replace value if key already exists

    def get(self, key):
        start_slot = self.hash_function(key)
        current_slot = start_slot

        while self.slots[current_slot] is not None:
            if self.slots[current_slot] == key:
                return self.data[current_slot]
            current_slot = self.rehash(current_slot)
            if current_slot == start_slot:
                return None

        return None

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

# Example usage
def has_datshit():
    h = HashTable(10)
    
    # Insert key-value pairs (strings)
    h["name"] = "John Doe"
    h["age"] = "30"
    h["city"] = "New York"
    
    # Retrieve values
    print(h["name"])  # Output: John Doe
    print(h["age"])   # Output: 30
    print(h["city"])
    h["age"] = "31"
    print(h["age"])
    print(h["country"])


has_datshit()

