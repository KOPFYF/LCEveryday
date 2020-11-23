class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Prefix Sum
        odd_sum = sum(x for i, x in enumerate(nums) if i % 2 == 1)
        even_sum = sum(nums) - odd_sum
                
        res, odd_presum, even_presum = 0, 0, 0
        for i, num in enumerate(nums):
            if not i % 2:
                # even index, even = left even + right odd
                even = even_presum + odd_sum - odd_presum
                even_presum += num
                odd = odd_presum + even_sum - even_presum
            else:
                # odd index, odd = left odd + right even
                odd = odd_presum + even_sum - even_presum
                odd_presum += num
                even = even_presum + odd_sum - odd_presum
            res += (even == odd)

        return res