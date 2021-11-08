class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for num in nums:
            bitmask ^= num
        
        rightmost_one = bitmask & (-bitmask) # right most 1
        group1, group2 = 0, 0
        for num in nums:
            # bitmask which will contain only x
            if num & rightmost_one:
                group1 ^= num
            else:
                group2 ^= num
        return [group1, group2]