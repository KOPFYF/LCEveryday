class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        This solution is great, but I'd like to point out one thing: this solution guarantees to find the min value, but not necessarily the correct pivot index!
e.g. [1,1,1,1,2,1,1], in this case, lo = 0 in the end, which is not the correct pivot index.
With this "bug", it may cause error if we use this directly in LC81 - Search in Rotated Sorted Array II
        '''
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # print(l, r, mid)
            if nums[mid] > nums[r]:
                # rotation pivot is on the right
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else: # nums[mid] == nums[r]
                if r > 0 and nums[r - 1] <= nums[r]:
                    r -= 1
                else:
                    # 1 1 1 1 1 1 1 1 2 (1) 1
                    # l                     r   
                    # l                  r     
                    return nums[r]
        
        return nums[l]
        
        # soln 2, value is right but the index could be wrong
        # When nums[mid] == nums[r], we couldn't sure the position of minimum
        # in mid's left or right, so just let upper bound reduce one.
        # Consider this case: 1 1 1 1 1 1 1 1 2 1 1
        # the min index returned is 0, while actually it should be 9.
        # For this case: 2 2 2 2 2 2 2 2 1 2 2
        # it will return the correct index, which is 8.
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # print(l, r, mid)
            if nums[mid] > nums[r]:
                # rotation pivot is on the right
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else: # nums[mid] == nums[r]
                r -= 1 # upper bound reduce one.
        
        return nums[l]