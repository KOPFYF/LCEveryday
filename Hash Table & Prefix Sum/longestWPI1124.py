class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # find the longest subarray with positive sum, O(n)/O(n)
        arr = [1 if hr > 8 else -1 for hr in hours]
        n = len(arr)
        
        d, presum, res = {}, 0, 0
        for i in range(n):
            presum += arr[i]
            if presum > 0:
                res = i + 1
            if presum not in d:
                d[presum] = i # the smallest index to get such presum
            if presum - 1 in d:
                res = max(res, i - d[presum - 1])
        return res