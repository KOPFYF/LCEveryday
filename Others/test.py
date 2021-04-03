class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        ans = mn0 = mn1 = nums[k]
        lo = hi = k
        while 0 <= lo-1 or hi+1 < len(nums): 
            if lo == 0 or hi+1 < len(nums) and nums[lo-1] < nums[hi+1]: hi += 1
            else: lo -= 1
            mn0 = min(mn0, nums[lo])
            mn1 = min(mn1, nums[hi])
            ans = max(ans, min(mn0, mn1)*(hi-lo+1))
        return ans