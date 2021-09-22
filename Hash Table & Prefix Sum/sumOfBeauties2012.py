class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        # O(n) / O(n), store left max and right min
        n = len(nums)
        mins = [float('inf') for _ in range(n)]
        min_ = float('-inf')
        for i in range(n):
            mins[i] = min_
            min_ = max(min_, nums[i])
            
        maxs = [float('-inf') for _ in range(n)]
        max_ = float('inf')
        for i in range(n-1, -1, -1):
            maxs[i] = max_
            max_ = min(max_, nums[i])
            
        # print(mins)
        # print(maxs)
        
        res = 0
        for i in range(1, n - 1):
            if mins[i] < nums[i] < maxs[i]:
                res += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                res += 1
        return res