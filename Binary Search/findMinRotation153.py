class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # print(l, r, mid)
            if nums[mid] > nums[r]:
                # rotation pivot is on the right
                l = mid + 1
            else:
                r = mid
        
        return nums[l]