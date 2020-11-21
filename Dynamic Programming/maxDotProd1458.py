class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        # dont init with 0 because nums could be negative
        dp = [[float('-inf')] * (n2 + 1) for _ in range(n1 + 1)]
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                prod = nums1[i - 1] * nums2[j - 1]
                # 4 cases, ignore nums1, ignore nums2, consider both, ignore neither
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + prod, prod)
        
        return dp[-1][-1] 


class Solution2:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i == 0 or j == 0: return float('-inf')  
            prod = nums1[i - 1] * nums2[j - 1]
            return max(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1) + prod, prod)
          
        return dfs(len(nums1), len(nums2))