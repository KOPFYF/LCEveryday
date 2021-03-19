class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        # prefix sum + binary search + 2 pointers
        presum = [0]
        for num in nums:
            presum.append(num + presum[-1])
        
        res, n = 0, len(nums)
        # prefix[i] <= prefix[j] - prefix[i] <= prefix[-1] - prefix[j]
        for i in range(1, n - 1):
            if presum[i] > presum[-1] // 3: 
                break
            # find the first pre_sum[j] so that pre_sum[j] >= 2 * pre_sum[i]
            j = bisect_left(presum, presum[i] * 2, i + 1, n)
            # find the last pre_sum[k] so that pre_sum[k] - pre_sum[i] <= total - pre_sum[k]
            # aka pre_sum[k] <= (total + pre_sum[i]) // 2 
            k = bisect_right(presum, presum[i] + (presum[-1] - presum[i]) // 2, j, n)
            res += k - j 
        
        return res % (10**9 + 7)