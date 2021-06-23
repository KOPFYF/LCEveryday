class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # advance i while n1[i] is bigger than n2[j], and increment j otherwise
        res, i = 0, 0
        for j, num2 in enumerate(nums2):
            while i < len(nums1) and nums1[i] > num2:
                i += 1
            if i == len(nums1):
                break
            res = max(res, j - i)
        return res