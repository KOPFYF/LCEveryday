class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = 0 
        prev = "a"
        for ch in word: 
            val = (ord(ch) - ord(prev)) % 26 
            prev = ch
            ans += min(val, 26 - val)
        return ans + len(word)