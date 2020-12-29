class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # O(n) recursion / divide-conquer
        d = collections.Counter(s)
        res = 0
        for c in set(s):
            if d[c] < k: # break with chars do not meet 
                for t in s.split(c):
                    res = max(res, self.longestSubstring(t, k))
                return res
        return len(s)
    
    
        # O(n) recursion / divide-conquer
        d = collections.Counter(s)
        for c in d:
            if d[c] < k: # break with chars do not meet 
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
    
        # O(n) iteration
        stack, res = [s], 0
        while stack:
            s = stack.pop()
            for c in set(s):
                # if Counter(s)[c] < k:
                if s.count(c) < k:
                    stack += [z for z in s.split(c)]
                    break # find a char and split
            else:
                res = max(res, len(s))
        return res
        
        
        # backtracking
        d = collections.Counter(s)
        i = 0
        res = 0
        for j, c in enumerate(s):
            if d[c] < k:
                # do not meet, break with current char and check [i:j]
                res = max(res, self.longestSubstring(s[i:j], k))
                i = j + 1
        return len(s) if i == 0 else max(res, self.longestSubstring(s[i:], k))
        
        
        
        