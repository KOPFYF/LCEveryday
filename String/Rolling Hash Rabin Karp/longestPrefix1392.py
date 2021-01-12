class Solution:
    def longestPrefix(self, s: str) -> str:
        l, r = 0, 0
        power = 1
        idx = 0
        n = len(s)
        nums = [ord(s[i]) - ord('a') for i in range(n)]
        mod = 10 ** 9 # without it TLE
        
        for i in range(n - 1):
            l = (l * 26 + nums[i]) % mod
            r = (r + power * nums[-i - 1]) % mod
            power = power * 26 % mod
            if l == r:
                idx = i + 1
                
        return s[: idx]