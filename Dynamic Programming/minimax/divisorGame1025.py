class Solution:
    def divisorGame(self, N: int) -> bool:
        @lru_cache(None)
        def dfs(n):
            if n == 1:
                return False
            res = False
            for i in range(1, n):
                if n % i == 0:
                    res |= not dfs(n - i)
            return res
        
        return dfs(N)

'''
https://leetcode.com/problems/divisor-game/discuss/274566/just-return-N-2-0-(proof)

prove it by two steps:

if Alice will lose for N, then Alice will must win for N+1, since Alice can first just make N decrease 1.
for any odd number N, it only has odd factor, so after the first move, it will be an even number
let's check the inference
fisrt N = 1, Alice lose. then Alice will must win for 2.
if N = 3, since all even number(2) smaller than 3 will leads Alice win, so Alice will lose for 3
3 lose -> 4 win
all even number(2,4) smaller than 5 will leads Alice win, so Alice will lose for 5
...

Therefore, Alice will always win for even number, lose for odd number.

'''
class Solution2:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0