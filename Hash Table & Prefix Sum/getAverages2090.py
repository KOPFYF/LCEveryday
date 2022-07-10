class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num) # presum[i] contains num[i-1]
        
        for i in range(n):
            if i - k >= 0 and i+k < n:
                s = presum[i+k+1] - presum[i-k]
                res[i] = s / (2*k + 1)
        return res


        res = [-1]*len(nums)

        left, windowSum, windowSize = 0, 0, 2*k+1
        for right in range(len(nums)):
            windowSum += nums[right]
            if (right-left+1 >= windowSize):
                res[left+k] = windowSum//windowSize
                windowSum -= nums[left]
                left += 1
        return res