class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2 * 6 or n2 > n1 * 6:
            return -1
        
        s1, s2 = sum(nums1), sum(nums2)
        if s1 > s2: # make sure s1 <= s2, and convert s1 to s2
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1
            
        hq1, hq2 = [], []
        for num1 in nums1:
            heapq.heappush(hq1, num1) # min heap, pop out min
        for num2 in nums2:
            heapq.heappush(hq2, -num2) # max heap, pop out max
            
        res = 0
        while s1 < s2:
            res += 1
            if len(hq2) == 0 or -hq2[0] - 1 < 6 - hq1[0]:
                # greedily use min(hq1), move it to 6
                s1 += 6 - heapq.heappop(hq1)
            else:
                s2 -= (-heapq.heappop(hq2) - 1)
        return res
        