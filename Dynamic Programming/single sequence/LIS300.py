class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP, time O(n^2) space O(n)
        # DP[i] means the result ends at i
        # So for dp[i], dp[i] is max(dp[j] + 1), for all j < i and nums[j] < nums[i]
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range (1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # print(dp)
        # [10,9,2,5,3,7,101,18]
        # [1, 1, 1, 2, 2, 3, 4, 4]
        return max(dp)

class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Top down DP, time O(n^2) space O(n)
        n = len(nums)
        @lru_cache(None)
        def dfs(i):
            if i == 0: return 1
            res = 1 # base case it's the element itself if no nums[j] < nums[i]
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(dfs(j) + 1, res) 
            return res
        
        return max(dfs(i) for i in range(n))


class Solution3(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Patience sorting, O(nlogn)
        # tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i]
        tails = []
        for h in nums:
            idx = bisect.bisect_left(tails, h)
            # if x is larger than all tails, append it, increase the size by 1
            if idx == len(tails):
                tails.append(h)
            # if tails[i-1] < x <= tails[i], update tails[i]
            else:
                tails[idx] = h
            # print(tails)
            # Input: [10,9,2,5,3,7,101,18], greedy search
            # [10]
            # [9]
            # [2]
            # [2, 5]
            # [2, 3]
            # [2, 3, 7]
            # [2, 3, 7, 101]
            # [2, 3, 7, 18]

        return len(tails)