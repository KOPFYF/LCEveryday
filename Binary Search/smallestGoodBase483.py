# https://leetcode.com/problems/smallest-good-base/discuss/96589/Java-solution-with-hand-writing-explain
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        # solve this equ: n*(x-1) = x^k - 1, x is the base, k is the length of 1
        # smallest good base of n => longest length of 1,  O(60*log(n))
        n = int(n)
        
        for k in range(60, 1, -1): # because n <= 10^18, log2(10 ^ 18 + 1) = 59.79471
            l, r = 2, n
            while l < r:
                x = (l + r) // 2
                left, right =  n*(x-1), x**k-1
                if left == right:
                    return str(x)
                elif left < right: # m is too large
                    r = x
                else: # m is too small
                    l = x + 1