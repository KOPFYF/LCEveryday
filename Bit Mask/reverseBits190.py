class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
            # print(bin(res)[2:], bin(n)[2:])
        return res