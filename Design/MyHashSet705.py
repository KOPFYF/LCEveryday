class MyHashSet:
    # Multiplicative hashing, many-to-one
    # https://en.wikipedia.org/wiki/Hash_function#Multiplicative_hashing.
    # hash function： h(k) = flool[(a k mod 2^w)/ 2^(w-m)], a = 1031237 or any odd num
    # which produces a hash value in [0, 2^m-1]
    # s % (2^t) = s & (1<<t) - 1
    # 10^4 operations so 2^m > 10000, m = 15

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]
        
    def _hash(self, key):
        return ((key * 1111111) & (1<<20) - 1) >> 5

    def _hash2(self, key):
        return key % len(self.arr)
        
    def add(self, key: int) -> None:
        val = self._hash(key)
        if key not in self.arr[val]:
            self.arr[val].append(key)

    def remove(self, key: int) -> None:
        val = self._hash(key)
        if key in self.arr[val]:
            self.arr[val].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.arr[self._hash(key)]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)