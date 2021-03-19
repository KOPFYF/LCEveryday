class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # hash table, O(n)/O(n)
        if k < 0:
            return 0
        res = 0
        counter = collections.Counter(nums)
        for key in counter:
            if k != 0:
                if key - k in counter:
                    res += 1
            else:
                if counter[key] > 1:
                    res += 1
        return res