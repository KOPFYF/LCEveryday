class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = i = 0
        d = {}
        for j in range(len(s)):
            while s[j] in d and d[s[j]] >= i:
                i = d[s[j]] + 1 # remove dup on the left end
            res = max(res, j - i + 1)
            d[s[j]] = j
        return res