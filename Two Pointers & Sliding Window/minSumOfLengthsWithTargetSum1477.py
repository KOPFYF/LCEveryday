class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # Sliding window + DP, time O(n) space O(n)
        n = len(arr)
        # dp[i] := length of smallest subarray in range arr[0]...arr[i] with sum = target
        dp = [float('inf')] * n 
        i, cumsum, res, bestever = 0, 0, float('inf'), float('inf')
        for j in range(n):
            cumsum += arr[j]
            while cumsum > target:
                cumsum -= arr[i]
                i += 1
            if cumsum == target:
                if i and dp[i - 1] != float('inf'):
                    # dp[i - 1] is the bestever for last window, != inf to check last win is valid
                    res = min(res, dp[i - 1] + j - i + 1)
                bestever = min(bestever, j - i + 1)
            dp[j] = bestever
        
        return res if res != float('inf') else -1