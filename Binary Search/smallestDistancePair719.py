class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def check(x):
            # use 2 pointers to track count
            cnt, i, j = 0, 0, 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= x:
                    j += 1 # move fast pointer
                cnt += j - i - 1
                i += 1 # move slow pointer
            return cnt >= k
        
        nums.sort()
        n = len(nums)
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            m = l + (r - l) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l