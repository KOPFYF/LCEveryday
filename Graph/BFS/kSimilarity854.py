class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        # The trick in this BFS is how to find all necessary neighbors efficiently.

        # remove all equal characters in the same indexes before BFS
        A_chars, B_chars = [], []
        for a, b in zip(A, B):
            if a != b:
                A_chars.append(a)
                B_chars.append(b)
        A = "".join(A_chars)
        B = "".join(B_chars)
        
        def get_neighbors(s):
            res = []
            for i in range(len(s) - 1):
                # greedy search the first mismatch index
                if s[i] == B[i]:
                    continue
                # find all possible chars to fix the first mismatch index
                for j in range(i + 1, len(s)):
                    if s[j] != B[j] and s[j] == B[i]:
                        # swap i and j and append to res
                        res.append(s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:])
                break
            return res
        
        queue, res, seen = [A], 0, set([A])
        while queue:
            new_queue = []
            for s in queue:
                if s == B:
                    return res
                for nei in get_neighbors(s):
                    # print(s, nei)
                    if nei not in seen:
                        seen.add(nei)
                        new_queue.append(nei)
            queue = new_queue
            res += 1

class Solution2:
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