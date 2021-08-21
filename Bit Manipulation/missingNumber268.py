class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # xor
        # a ^ 0 = a
        # a ^ a = 0
        n, xor = len(nums), 0
        for i in range(n + 1):
            xor ^= i
        
        for num in nums:
            xor ^= num 
        return xor
    
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing