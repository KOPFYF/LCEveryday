class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        # We can treat each string as a node. 
        # If two strings x and y differ by one swap and that swap makes x more simliar to target string B, there is a directed edges between them.
        # generate all children node of a node x. Each child node requires one swap to change from x and each child node has one character more similiar to B than x
        
        def nei(x):
            i = 0
            while x[i] == B[i]: 
                i += 1 # first index of diff 
            for j in range(i + 1, len(x)):
                if x[j] == B[i] and x[j] != B[j]: # first index we can swap
                    # swap i and j
                    yield x[:i] + x[j] + x[i+1:j] + x[i] + x[j+1:]
                    
        q, seen = [(A, 0)], {A}
        for x, d in q:
            if x == B: 
                return d
            for y in nei(x): # loop all neighbors of x
                if y not in seen:
                    seen.add(y), 
                    q.append((y, d + 1))