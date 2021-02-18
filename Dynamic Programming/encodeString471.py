'''
https://leetcode.com/problems/encode-string-with-shortest-length/discuss/375160/Concise-Python-detailed-explanation
For any s, you can either

1. Do not encode it
2. Or encode it to one string if possible

"i=(s+s).find(s,1)"
"i" is the length of repeating pattern. If i>=len(s), then s is not repeated.

3. Or, split it into two, encode the two substring to their shortest possible length, and combine them

Pick up the shortest result from 1~3.

'''


class Solution:
    @lru_cache(None)
    def encode(self, s: str) -> str:
        # DP, O(n^3)
        i = (s + s).find(s, 1)
        if i < len(s):
            encoded = str(len(s) // i) + '[' + self.encode(s[:i]) + ']'
        else:
            encoded = s
        
        res = encoded
        min_len = len(encoded)
        for i in range(1, len(s)):
            tmp = self.encode(s[:i]) + self.encode(s[i:])
            if len(tmp) < min_len:
                min_len = len(tmp)
                res = tmp
        return res
    
        # splitEncoded=[self.encode(s[:i])+self.encode(s[i:]) for i in range(1,len(s))]
        # res = min(splitEncoded + [encoded], key=len)
        # # print(res, splitEncoded, encoded)
        # return res