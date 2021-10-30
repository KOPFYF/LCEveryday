class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1: Brute force O(nlogn), but abey rules
        n = len(nums)
        if n == 2: return nums[0]
        nums.sort()
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return nums[i]
        
        # Solution 2: two pointer, O(n)/O(1), fastest
        # Floyd's Tortoise and Hare (Cycle Detection), 2(F+a)=F+nC+a => F+a=nC
        slow = nums[0]
        fast = nums[nums[0]]
        # find meeting point in the cycle
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow
        
        # Solution 3: binary search O(nlogn), no need to sort
        # Pigeonhole Principle (https://en.wikipedia.org/wiki/Pigeonhole_principle) 
        # applying bi-search in the range[1, n] by counting the element which falls in sub range(n/2, n]
        # one of them has occurred more than once.
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r-l) // 2
            cnt = 0
            for i in nums:
                if i <= m:
                    cnt += 1
            if cnt <= m:
                l = m + 1
            else:
                r = m
        return l