class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        res, max_l, min_r, n = 0, float('-inf'), float('inf'), len(nums)
        found = [0] * 100001
        for i in range(n):
            found[i] = max_l < nums[i]
            max_l = max(max_l, nums[i])
        
        for i in range(n - 1, -1, -1):
            res += int(found[i] and nums[i] < min_r)
            min_r = min(min_r, nums[i])
        
        return res


class Solution2:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        prefix = [False] * n                  # Create prefix array and initialize them as False
        cur_max, cur_min = nums[0], nums[-1]  # Initialize prefix_max & suffix_min
        for i in range(n):                    # Update prefix from left to right
            prefix[i] = cur_max <= nums[i] 
            cur_max = max(cur_max, nums[i])
        for i in range(n-1, -1, -1):          # Update suffix and count from right to left
            prefix[i] &= cur_min >= nums[i]   # Use `&` operation (`and` is also fine) to make sure 2 condition hold at the same time
            ans += prefix[i]                  # +1 when `prefix[i]` is True, otherwise +0 (no change)
            cur_min = min(cur_min, nums[i])    
        return ans