class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # O(mnlogk)
        hq = []
        for n1 in nums1:
            for n2 in nums2:
                if len(hq) < k:
                    heapq.heappush(hq, (-n1-n2, [n1, n2]))
                else:
                    heapq.heappushpop(hq, (-n1-n2, [n1, n2]))
        return [ran for s, ran in hq]