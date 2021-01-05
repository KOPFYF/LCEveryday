class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix = [0]
        for x in nums: 
            prefix.append(prefix[-1] + x)
        
        res = 0
        # prefix[i] <= prefix[j] - prefix[i] <= prefix[-1] - prefix[j]
        for i in range(1, len(nums)): # left = nums[:i]
            j = bisect_left(prefix, 2 * prefix[i])
            k = bisect_right(prefix, (prefix[i] + prefix[-1]) // 2)
            res += max(0, min(len(nums), k) - max(i + 1, j))
        return res % (10**9 + 7)
  
  
class Solution2:
    def waysToSplit(self, nums: List[int]) -> int:    
        presum = [0]
        for n in nums:
            presum.append(n + presum[-1])
        
        res = 0
        # prefix[i] <= prefix[j] - prefix[i] <= prefix[-1] - prefix[j]
        for start1 in range(1,len(nums)-1):
            if presum[start1] > presum[-1] // 3: 
                break
            # find the first pre_sum[j] so that pre_sum[j] >= 2 * pre_sum[i]
            start2_lower = max(start1 + 1, \
                               bisect_left(presum, presum[start1] * 2))
            # find the last pre_sum[k] so that pre_sum[k] - pre_sum[i] <= total - pre_sum[k]
            # aka pre_sum[k] <= (total + pre_sum[i]) // 2 
            start2_upper = min(len(nums), \
                               bisect_right(presum, presum[start1] + (presum[-1] - presum[start1]) // 2))
            res += start2_upper - start2_lower 
        
        return res % (10**9 + 7)