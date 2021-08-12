class Solution:
    def addStrings(self, nums1: str, nums2: str) -> str:
        i, j = len(nums1) - 1, len(nums2) - 1
        carrier, res = 0, ""
        while i >= 0 or j >= 0 or carrier:
            if i >= 0:
                carrier += int(nums1[i])
            if j >= 0:
                carrier += int(nums2[j])
            res = str(carrier % 10) + res
            carrier //= 10
            i -= 1
            j -= 1
        return res