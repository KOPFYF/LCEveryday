class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # sort, Subsequences does not matter cause we care min/max only
        # 2 sum, 2 ptrs, O(nlogn + n) / O(1)
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        mod = 10**9 + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                # res += pow(2, r - l) # TLE!
                res += pow(2, r - l, mod)
                # res += 2**(r-l) % mod
                l += 1
        return res % mod