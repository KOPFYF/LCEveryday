class Solution:
    def jump(self, nums: List[int]) -> int:
        # Same as 763. Partition Labels
        if len(nums) <= 1: 
            return 0
        res = 1
        l, r = 0, nums[0]
        
        while r < len(nums) - 1:
            res += 1
            nxt = max(i + nums[i] for i in range(l, r+1))
            l, r = r, nxt # grow the range by trying all
        
        return res