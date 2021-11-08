class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
        binary search O(logn)
        check mid is even or odd
        if mid is even, then it's duplicate should be in next index.
        if mid is odd, then it's duplicate  should be in previous index.
        
        '''
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # if mid is even, then it's duplicate should be in next index.
            # if mid is odd, then it's duplicate should be in previous index.
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) \
            or (mid % 2 == 0 and nums[mid + 1] == nums[mid]):
                l = mid + 1
            else:
                r = mid
        return nums[l]
    
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # if mid is even, then it's duplicate should be in next index.
	        # if mid is odd, then it's duplicate should be in previous index.
            if (mid % 2 == 1 and mid - 1 >= 0 and nums[mid - 1] == nums[mid]) \
            or (mid % 2 == 0 and mid + 1 < len(nums) and nums[mid + 1] == nums[mid]):
                l = mid + 1
            else:
                r = mid
        return nums[l]


        # XOR, O(n)/O(1)
        res = 0
        for num in nums:
            res ^= num
        return res