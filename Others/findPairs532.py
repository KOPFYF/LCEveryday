class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # hash table
        if k < 0:
            return 0
        res = 0
        counter = collections.Counter(nums)
        for key in counter:
            if k != 0:
                if key - k in counter:
                    res += 1
            else:
                if counter[key] > 1:
                    res += 1
        return res
    
        # 2 pointers
        nums.sort()
        i, j, n = 0, 1, len(nums)
        res = 0
        while i < n and j < n:
            if j < n and nums[j] - nums[i] > k:
                i += 1
            elif i == j or nums[j] - nums[i] < k:
                j += 1
            else:
                res += 1
                i += 1
                while i < n and nums[i] == nums[i - 1]: # dedup
                    i += 1
        return res