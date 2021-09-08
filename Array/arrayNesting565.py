class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # O(n) / O(1)
        res = 0
        for x in nums:
            if x == -1: 
                continue
            cnt = 0
            while nums[x] != -1:
                cnt += 1
                nums[x], x = -1, nums[x] # set visited as -1
            res = max(res, cnt)
                
        return res
        
        
        # O(n) / O(n)
        n = len(nums)
        seen = [0] * n
        res = 0
        for num in nums:
            cnt = 0
            while not seen[num]:
                cnt += 1
                seen[num] = 1
                num = nums[num]
            res = max(res, cnt)
        return res