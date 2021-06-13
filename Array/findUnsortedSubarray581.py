class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # O(n)
        n = len(nums)
        beg, end = -1, -2
        minm, maxm = nums[-1], nums[0]
        for i in range(n):
            maxm = max(maxm, nums[i])
            minm = min(minm, nums[n-i-1])
            if nums[i] < maxm:
                end = i
            if nums[n-1-i] > minm:
                beg = n - 1 - i
        return end - beg + 1
        
        
        # O(nlogn)
        nums_st = sorted(nums)
        n = len(nums)
        
        l,r = 0,-1
        for i in range(n):
            if nums[i] != nums_st[i]:
                l = i
                break
        for i in range(n-1, 0, -1):
            if nums[i] != nums_st[i]:
                r = i
                break
        return r-l+1