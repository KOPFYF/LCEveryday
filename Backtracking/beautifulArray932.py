'''
Saying that an array is beautiful,
there is no i < k < j,
such that A[k] * 2 = A[i] + A[j]

Apply these 3 following changes a beautiful array,
we can get a new beautiful array


1. Deletion
Easy to prove.

2. Addition
If we have A[k] * 2 != A[i] + A[j],
(A[k] + x) * 2 = A[k] * 2 + 2x != A[i] + A[j] + 2x = (A[i] + x) + (A[j] + x)

E.g: [1,3,2] + 1 = [2,4,3].

3. Multiplication
If we have A[k] * 2 != A[i] + A[j],
for any x != 0,
(A[k] * x) * 2 = A[k] * 2 * x != (A[i] + A[j]) * x = (A[i] * x) + (A[j] * x)

E.g: [1,3,2] * 2 = [2,6,4]


A1 = A * 2 - 1 is beautiful with only odds from 1 to N * 2 -1
A2 = A * 2 is beautiful with only even from 2 to N * 2
B = A1 + A2 beautiful array with length N * 2
'''

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        memo = {1: [1]}
        def dfs(n):
            if n not in memo:
                odds = dfs((n + 1) // 2)
                evens = dfs(n // 2)
                memo[n] = [2*x-1 for x in odds] + [2*x for x in evens]
            return memo[n]
        # print(dfs(2)) # [1, 2]
        # print(dfs(3)) # [1, 3, 2]
        # print(dfs(4)) # [1, 3, 2, 4]
        # print(dfs(5)) # [1, 5, 3, 2, 4]
        return dfs(n)