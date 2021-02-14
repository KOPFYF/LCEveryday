class Solution:
    def countVowelStrings(self, n: int) -> int:
        # soln 1
        return comb(n + 4,4)
        
        # soln 2
        #            a  e  i  o  u
        # initialy: {1, 1, 1, 1, 1}   
        # n == 1 : {5, 4, 3, 2, 1}   
        # n == 2 : {15,10,6, 3, 1}   
        # n == 3 : {35,20,10,4, 1}
        dp = [1, 1, 1, 1, 1]
        for _ in range(n):
            for j in range(4, 0, -1):
                dp[j - 1] += dp[j]
        
        return dp[0]