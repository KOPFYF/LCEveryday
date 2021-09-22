class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        for i in range(n-2, -1, -1):
            shifts[i] += shifts[i+1]
            
        res = ""
        def shifting(ch, shift):
            idx = (ord(ch) - ord('a') + shift) % 26
            return chr(idx + ord('a'))
            # return chr((ord(ch) + shift) % 26)
        
        for ch, shift in zip(s, shifts):
            res += shifting(ch, shift)
        return res