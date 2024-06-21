class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i, j, n = 0, 0, len(nums)
        maxFreq, res = 0, 0
        dic = defaultdict(int)
        while j < n:
            # grow right
            dic[nums[j]] += 1
            while dic[nums[j]] > k:
                # shrink left
                dic[nums[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
            j += 1
        
        return res