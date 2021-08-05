class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # buy & sell stocks, 5 states, O(n) / O(n)
        # a -> e
        # e -> a/i
        # i -> a/e/o/u
        # o -> i/u
        # u -> a
        # dp will store the number of strings of length i that end in each vowel accordingly
        dp_a = [1] * n
        dp_e = [1] * n
        dp_i = [1] * n
        dp_o = [1] * n
        dp_u = [1] * n
        mod = 10**9 + 7
        
        for i in range(1, n):
            dp_a[i] = (dp_e[i - 1] + dp_i[i - 1] + dp_u[i - 1]) % mod
            dp_e[i] = (dp_a[i - 1] + dp_i[i - 1]) % mod
            dp_i[i] = (dp_e[i - 1] + dp_o[i - 1]) % mod
            dp_o[i] = (dp_i[i - 1]) % mod
            dp_u[i] = (dp_i[i - 1] + dp_o[i - 1]) % mod
        
        return (dp_a[-1] + dp_e[-1] + dp_i[-1] + dp_o[-1] + dp_u[-1]) % mod