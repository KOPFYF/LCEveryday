class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # O(n)/O(26)
        d1, d2 = {}, {}
        for ch1, ch2 in zip(s, t):
            if ch1 not in d1 and ch2 not in d2:
                d1[ch1] = ch2
                d2[ch2] = ch1
            elif d1.get(ch1) != ch2 or d2.get(ch2) != ch1:
                return False
        return True