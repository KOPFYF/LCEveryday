class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.left, self.right = False, False
        def bisect_left(nums, target):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    if nums[mid] == target:
                        self.left = True
                    r = mid
            return l
        
        def bisect_right(nums, target):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    if nums[mid] == target:
                        self.right = True
                    l = mid + 1
                else:
                    r = mid
            return l
        
        i, j = bisect_left(nums, target), bisect_right(nums, target)
        # print(i, j, self.left, self.right)
        if self.left:
            return [i, j-1]
        else:
            return [-1, -1]



class Solution2:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bisect_left(nums, target):
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l
        idx1 = bisect_left(nums, target)
        idx2 = bisect_left(nums, target + 1) - 1
        if idx1 < len(nums) and nums[idx1] == target:
            return [idx1, idx2]
        else:
            return [-1, -1]

            