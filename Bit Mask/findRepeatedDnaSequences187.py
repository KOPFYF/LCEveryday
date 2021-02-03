class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10: return []
        
        digits = {"A": 0, "C": 1, "G": 2, "T": 3} # 4 jin zhi
        mask = 0xfffff # 20 ones
        pattern = 0
        seen, res = set(), set()
        for i, ch in enumerate(s):
            # pattern shift left twice
            pattern = (pattern << 2 | digits[ch]) & mask
            if i >= 9:
                if pattern in seen:
                    res.add(s[i-9:i+1])
                else:
                    seen.add(pattern)
        return res