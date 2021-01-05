class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # based on 239 Sliding Window Maximum, sliding win max + dp
        # dp[i] = max(dp[i - k], dp[i - k + 1], ..., dp[i - 1], 0) + num
        # dp[i]: max sum from nums[:i]
        # deque: stores dp[i - k], dp[i-k+1], .., dp[i - 1] with val > 0 in a dec order
        dp = nums[:1] # base case
        mono_dec = collections.deque(dp)
        for i, num in enumerate(nums[1:], 1):
            # 1. remove header out of win based on k
            if i > k and mono_dec[0] == dp[i - k - 1]:
                mono_dec.popleft() 
            # 2. dp bottom up
            tmp = max(mono_dec[0] + num, num) 
            dp.append(tmp)
            # 3. maintain a mono dec deque
            while mono_dec and mono_dec[-1] < tmp:
                mono_dec.pop()
            mono_dec.append(tmp)   
            # print(i, num, tmp, dp, mono_dec)
        return max(dp)  