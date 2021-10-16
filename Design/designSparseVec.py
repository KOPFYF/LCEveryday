import collections
import math


class SparseVector:
    def __init__(self, dim):
        self.dim = dim
        self.hash = collections.defaultdict(int)


    def set(self, value, index):
        if index >= self.dim:
            raise ValueError("Out of range!")
        self.hash[index] = value


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        if vec.dim != self.dim:
            raise ValueError("The dimensions of two vectors mismatch!")
        res = 0
        # Iterate over the vector with fewer non-zero numbers.
        if len(vec.hash) >= len(self.hash):
            for i, num in self.hash.items():
                res += num * vec.hash[i]
        else:
            for i, num in vec.hash.items():
        res += num * self.hash[i]
         
        return res


    def addition(self, vec):
        if vec.dim != self.dim:
            raise ValueError("The dimensions of two vectors mismatch!")
        res = [0] * self.dim
        for i, num in self.hash.items():
            res[i] += num
        for i, num in vec.hash.items():
            res[i] += num
        return res


    def cosine(self, vec):
        def norm(v):
            res = 0
            for num in v.values():
                res += num * num
            return math.sqrt(res)
            
        res = self.dotProduct(vec)
        res /= (norm(vec.hash) * norm(self.hash))
        return res


sv = SparseVector(100)
sv2 = SparseVector(100)
sv.set(5, 10)
sv.set(10, 11)
sv2.set(5, 10)
sv2.set(10, 12)