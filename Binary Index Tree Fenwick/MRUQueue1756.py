class MRUQueue:

    def __init__(self, n: int):
        self.size = n
        self.tree = FenwickTree(n + 2000)
        self.vals = [0] * (n + 2000)
        for i in range(n):
            self.tree.update(i + 1, 1)
            self.vals[i] = i + 1

    def fetch(self, k: int) -> int:
        l, r = 0, self.size
        while l < r:
            mid = (l + r) // 2
            if self.tree.query(mid) < k:
                l = mid + 1
            else: 
                r = mid
        self.tree.update(l, -1)
        self.tree.update(self.size+1, 1)
        self.vals[self.size] = self.vals[l-1]
        self.size += 1
        return self.vals[l-1]
        
        

class FenwickTree:
    def __init__(self, n):
        self.sums = [0] * (n + 1)


    def update(self, i, delta):
        # go down
        while i < len(self.sums):
            self.sums[i] += delta
            i += self._lowbit(i)


    def query(self, i):
        # go up/go to parent
        s = 0
        while i > 0:
            s += self.sums[i]
            i -= self._lowbit(i)
        return s


    def _lowbit(self, x):
        # return x & (~x + 1)
        return x & -x 