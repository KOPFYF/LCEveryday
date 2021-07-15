class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        [4,5,6,7,0,1,2], rotated at pivot index 3
        0
        -> 4
        -1 if it is not in nums
        
          - (6)      
         - (5)
        - (4)
        '''
        # if sorted

        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid 
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        if nums[l] == target:
            return l
        return -1