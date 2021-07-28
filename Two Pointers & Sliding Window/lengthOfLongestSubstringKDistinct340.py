import collections

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = collections.Counter()
        res = i = 0
        for j in range(len(s)):
            if count[s[j]] == 0: 
                k -= 1
            count[s[j]] += 1
            while k < 0:
                count[s[i]] -= 1
                if count[s[i]] == 0: 
                    k += 1
                i += 1
            res = max(res, j - i + 1)
        return res