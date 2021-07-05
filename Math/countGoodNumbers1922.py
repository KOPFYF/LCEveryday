class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # (A * B) % m = ((A % m) * (B % m)) % m
        # pattern 5*4*5*4*5*4*5..... ans so on
        # https://stackoverflow.com/questions/48839772/why-is-time-complexity-o1-for-powx-y-while-it-is-on-for-xy
        mod = 10**9 + 7
        return pow(5, (n + 1) // 2, mod) * pow(4, n // 2, mod) % mod