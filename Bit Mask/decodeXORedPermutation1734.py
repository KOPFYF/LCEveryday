class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        # key: find the first element
        # encoded = [a0^a1, a1^a2, a2^a3, a3^a4, a4^a5]
        start, other = 0, 0
        for i in range(1, len(encoded) + 2): # (a0^a1^a2^a3^a4^a5)
            start ^= i
            
        for i, val in enumerate(encoded):
            if i % 2: 
                other ^= val
            
        res = [start ^ other]
        for encode in encoded:
            res.append(encode ^ res[-1])
        return res