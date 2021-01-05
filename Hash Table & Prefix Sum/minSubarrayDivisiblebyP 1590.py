class Solution(object):
    def minSubarray(self, A, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        need = sum(A) % p
        dp = {0 : -1} # record the latest index of mod results so that we get shortest subarray
        cur = 0
        res = len(A)
        
        for i, a in enumerate(A):
            cur = (cur + a) % p
            dp[cur] = i
            if (cur - need) % p in dp:
                # we found the subarray as needed to exclude
                res = min(res, i - dp[(cur - need) % p])
        return res if res < len(A) else -1