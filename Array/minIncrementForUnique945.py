class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # [5,5,5] -> [5,6,7], len=3, max=5, till 7
        # counter, O(max+len)/O(max+len)
        max_num = max(nums)
        cnt = Counter(nums)
        taken = []
        res = 0
        
        for x in range(len(nums) + max_num):
            if cnt[x] >= 2:
                taken += [x] * (cnt[x] - 1) # redundent
            elif taken and cnt[x] == 0:
                res += x - taken.pop()
        return res
        
        
        
        # sort O(nlogn)
        if not nums:
            return 0
        nums.sort()
        s, res = nums[0], 0
        for num in nums:
            print(res, s)
            res += max(0, s - num)
            s = max(s + 1, num + 1) # jump
        print(res, s)    
        return res