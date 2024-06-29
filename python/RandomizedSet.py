import random

class RandomizedSet:

    def __init__(self):
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        self.data.remove(val)
        return True

    def getRandom(self) -> int:

        return random.choice(self.data)
    
randomized_set = RandomizedSet()

# Test insert
print(randomized_set.insert(1))  # Should print True
print(randomized_set.insert(2))  # Should print True
print(randomized_set.insert(2))  # Should print False

# Test getRandom
print(randomized_set.getRandom())  # Should print either 1 or 2

# Test remove
print(randomized_set.remove(1))  # Should print True
print(randomized_set.remove(1))  # Should print False
print(randomized_set.getRandom())