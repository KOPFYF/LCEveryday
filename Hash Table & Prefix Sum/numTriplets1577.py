'''
Precalculate the frequencies of all nums1[i]^2 and nums2[i]^2
'''
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # Precalculate the frequencies of all nums1[i]^2 and nums2[i]^2
        # O(m^2 + n^2), 1 <= m, n <= 1000
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        m, n = len(nums1), len(nums2)
        
        for num1 in nums1:
            d1[num1 ** 2] += 1
        for num2 in nums2:
            d2[num2 ** 2] += 1

        res = 0
        for i in range(m - 1):
            for j in range(i + 1, m):
                res += d2[nums1[i] * nums1[j]]
                
        for i in range(n - 1):
            for j in range(i + 1, n):
                res += d1[nums2[i] * nums2[j]]
        
        return res