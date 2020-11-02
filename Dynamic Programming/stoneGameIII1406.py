class Solution1(object):
    def stoneGameIII(self, A):
        """
        :type stoneValue: List[int]
        :rtype: str
        """    
        # DFS + memo, 4936 ms
        res = self.dfs(A, 0, {})
        return 'Tie' if res == 0 else 'Alice' if res > 0 else 'Bob'
        
    def dfs(self, A, pos, memo):
        if pos >= len(A):
            return 0
        if pos in memo:
            return memo[pos]

        memo[pos], Alice = float('-inf'), 0
        for j in range(pos, min(pos + 3, len(A))):
            Alice += A[j]
            memo[pos] = max(memo[pos], Alice - self.dfs(A, j + 1, memo))
        return memo[pos]


class Solution2(object):
	def stoneGameIII(A):
		"""
        :type stoneValue: List[int]
        :rtype: str
        """  
		# bottom up DP, without compression
        # Time O(n^2), Space O(n)
		dp = [0] * (len(A) + 3)
		for i in range(len(A) - 1, -1, -1):
		    dp[i] = max(sum(A[i:i + k]) - dp[i + k] for k in range(1, 4))
		return "Alice" if dp[0] > 0 else "Bob" if dp[0] < 0 else "Tie"


class Solution3(object):
    def stoneGameIII(self, A):
        """
        :type stoneValue: List[int]
        :rtype: str
        """  
        # bottom up DP, with compression
        # Time O(n^2), Space O(1)
        dp = [0] * 3
        for i in xrange(len(A) - 1, -1, -1): 
            # reverse from right end because base case on the right
            dp[i % 3] = max(sum(A[i:i + k]) - dp[(i + k) % 3] for k in range(1, 4))
        return ["Tie", "Alice", "Bob"][cmp(dp[0], 0)]



