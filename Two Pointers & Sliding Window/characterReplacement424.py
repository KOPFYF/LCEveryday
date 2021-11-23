class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        res = 0
        i = 0
        
        for j, ch in enumerate(s):
            dic[ch] += 1
            while i < j and j - i + 1 - max(dic.values()) > k:
                # in this window, other than most freq char
                dic[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res