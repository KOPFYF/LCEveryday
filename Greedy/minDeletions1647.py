class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {} # frequency table 
        for c in s: freq[c] = 1 + freq.get(c, 0)
        
        ans = 0
        seen = set()
        for k in sorted(freq.values(), reverse=True): 
            while k in seen: 
                k -= 1 
                ans += 1
            if k: 
                seen.add(k)
        return ans 


class Solution1:
    def minDeletions(self, s: str) -> int:
        # greedy
        cnt, res, used = collections.Counter(s), 0, set()
        for ch, freq in cnt.items():
            while freq > 0 and freq in used: # while loop + set
                freq -= 1
                res += 1
            used.add(freq)
        return res