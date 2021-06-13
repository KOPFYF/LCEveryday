class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        => nums1[i] - nums2[i] > nums2[j] - nums1[j]
        => (nums1[i] - nums2[i]) - (nums2[j] - nums1[j]) > 0
        => (nums1[i] - nums2[i]) + (nums1[j] - nums2[j]) > 0
        
        =>
        define nums = [nums1[0]-nums2[0], nums1[1]-nums2[1], ...]
        How many (i, j) pairs with i < j that nums[i] + nums[j] > 0
        
        =>
        Given a value x, count the number of y in the nums that satisfies (y + x > 0)
        => y > -x => y >= -x+1
        '''
        res, n = 0, len(nums1)
        nums = [x1 - x2 for x1, x2 in zip(nums1, nums2)]
        nums.sort()
        
        for i, x in enumerate(nums):
            idx = bisect.bisect_left(nums, - x + 1)
            res += n - max(i + 1, idx)
        return res
            