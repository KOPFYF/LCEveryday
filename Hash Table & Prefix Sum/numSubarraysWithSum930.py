class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        # prefix sum convert to 2 sum
        cnt = defaultdict(int)
        cnt[0] = 1
        res, prefix = 0, 0
        for a in A:
            prefix += a
            res += cnt[prefix - S]
            cnt[prefix] += 1
        return res