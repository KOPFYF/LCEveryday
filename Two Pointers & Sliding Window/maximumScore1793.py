class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = mini = nums[k]
        i, j, n = k, k, len(nums)
        while i > 0 or j < n - 1:
            if i > 0 and j < n - 1 and nums[i - 1] < nums[j + 1]:
                j += 1
            elif i > 0 and j < n - 1 and nums[i - 1] > nums[j + 1]:
                i -= 1
            elif i == 0 and j < n - 1:
                j += 1
            else: # i > 0 and j == n - 1: # TLE
                i -= 1
            mini = min(mini, nums[i], nums[j])
            res = max(res, mini * (j - i + 1))
            # print(i, j, mini, res)
        return res
    
        res = lmin = rmin = nums[k]
        n = len(nums)
        i = j = k
        while i >= 1 or j < n - 1: 
            if i == 0 or j + 1 < n and nums[i-1] < nums[j+1]: 
                j += 1
            else: 
                i -= 1
            lmin = min(lmin, nums[i])
            rmin = min(rmin, nums[j])
            res = max(res, min(lmin, rmin) * (j - i + 1))
        return res
    
        res = mini = nums[k]
        i, j, n = k, k, len(nums)
        while i > 0 or j < n - 1:
            if (nums[i - 1] if i else 0) < (nums[j + 1] if j < n - 1 else 0):
                j += 1
            else:
                i -= 1
            mini = min(mini, nums[i], nums[j])
            res = max(res, mini * (j - i + 1))
            # print(i, j, mini, res)
        return res