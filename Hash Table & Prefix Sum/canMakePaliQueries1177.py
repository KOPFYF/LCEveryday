class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        # TLE for brute force
        # prefix sum will do. DP cache!
        n = 26
        dp = [[0] * n] # dp[i] represents the count of all the letters in s[:i]
        for i in range(len(s)):
            new = dp[i][:]
            j = ord(s[i]) - ord('a')
            new[j] += 1
            dp.append(new)
        # print(dp) # len(s) * 26
        
        res = []
        for l, r, k in queries:
            left, right = dp[l], dp[r + 1]
            cnt = sum((left[i] - right[i]) % 2 for i in range(n))
            res.append(cnt // 2 <= k)
        return res