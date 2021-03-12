class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Bit mask & hash map, like 2 sum, O(5n)/O(n)
        mask = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        d, n, res = {0: -1}, 0, 0
        for i, c in enumerate(s):
            if c in mask:
                # XOR, 4a, 3e, 2i, 1o, 0u would be 01010
                # n would be 0 if count is even
                n ^= mask[c] 
            if n not in d:
                d[n] = i # the latest index for bit pattern n
            else:
                res = max(res, i - d[n]) # retrieve last seen pattern
            # print(bin(n)[2:], n, i, d, r)
        return res