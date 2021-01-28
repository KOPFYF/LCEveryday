class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        # encoded[i] = perm[i] XOR perm[i + 1]
        # perm[i] = perm[i-1] XOR encoded[i-1]
        # For example, original list is[a1, a2, a3, a4, a5], 
        # which means encoded list is [a1^a2, a2^a3, a3^a4, a4^a5].
        # We can get a1^a2, a1^a3, a1^a4, a1^a5 after iterating encoded list.
        # And we can compute a1^a2^a3^a4^a5 beforehand.
        # Then by xor all of them we can get the first element a1:
        # (a1^a2) ^ (a1^a3) ^ (a1^a4) ^ (a1^a5) ^ (a1^a2^a3^a4^a5) = a1
        
        # For example, original [2, 4, 1, 5, 3]:
        # After iterating encoded list, we have 2 ^ 4, 2 ^ 1, 2 ^ 5, 2 ^ 3 in hand.
        # And we can get 1 ^ 2 ^ 3 ^ 4 ^ 5 by problem definition.
        # So (2 ^ 4) ^ (2 ^ 1) ^ (2 ^ 5) ^ (2 ^ 3) ^ (1 ^ 2 ^ 3 ^ 4 ^ 5) = 2, which is the start element.
        
        start = 0
        for i in range(1, len(encoded) + 2): # (a1^a2^a3^a4^a5)
            start ^= i
        curr = 0
        for encode in encoded:
            curr ^= encode # a2^a3
            start ^= curr # a1^a2^a2^a3 = a1^a3
        res = [start]
        for encode in encoded:
            res.append(encode ^ res[-1])
        return res