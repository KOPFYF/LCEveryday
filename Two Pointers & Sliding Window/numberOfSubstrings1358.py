class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # sliding window
        i = 0
        res = 0
        n = len(s)
        count = {c: 0 for c in 'abc'}
        for j in range(n):
            count[s[j]] += 1
            while all(count.values()):
                count[s[i]] -= 1
                i += 1
            # [i-1 .. j] represents min length sub-array ending at j which has all three characters.
            # this subarray could be extended left till idx == 0 without compromising the count constraint
            res += i
        return res