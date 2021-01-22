class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        word_set = set()
        for w1, w2 in pairs:
            word_set.add(w1)
            word_set.add(w2)
        n = len(word_set)
        dsu = DSU(n)
        word_dict = {w:i for i, w in enumerate(list(word_set))}
        for w1, w2 in pairs:
            dsu.union(word_dict[w1], word_dict[w2])
            
        for q1, q2 in zip(words1, words2):
            if q1 == q2:
                continue
            if q1 not in word_set or q2 not in word_set:
                return False
            if dsu.find(word_dict[q1]) != dsu.find(word_dict[q2]):
                return False
        return True
            
                            
class DSU(object):
    # Union by size
    def __init__(self, n):
        self.parents = [0] * n
        self.size = [1] * n
        for i in range(n):
            self.parents[i] = i
    
    def find(self, x):
        # Path compression
        if self.parents[x] != x: # if x is nott root
            self.parents[x] = self.find(self.parents[x]) # recursion
        return self.parents[x]
    
    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return
        if self.size[rootx] <= self.size[rooty]:
            self.parents[rootx] = rooty
            self.size[rooty] += self.size[rootx]
        else:
            self.parents[rooty] = rootx
            self.size[rootx] += self.size[rooty]
            
    def isConnect(self, x, y):
        return self.find(x) == self.find(y)