class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        '''
        2 3 3 5
        
        2 3 4 4 5 6
        '''
        n = len(nums)
        res = float('-inf')
        nums.sort()
        for i in range(n//2):
            # print(i, nums[i], nums[n-i-1])
            res = max(res, nums[i] + nums[n-i-1])
        return res