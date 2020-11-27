class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # This is an elementary dynamic programming problem.
        # odd[i] records the number of subarray ending at arr[i] that has odd sum.
        # even[i] records the number of subarray ending at arr[i] that has even sum.
        # if arr[i + 1] is odd, odd[i + 1] = even[i] + 1 and even[i + 1] = odd[i]
        # if arr[i + 1] is even, odd[i + 1] = odd[i] and even[i + 1] = even[i] + 1
        
        res = odd = even = 0
        for a in arr:
            even += 1 # why not odd += 1? Cause the first sum is 0, so even should lead
            if a % 2:
                # flip count if only we see an odd
                odd, even = even, odd
            res = (res + odd) % (10**9 + 7)             
        return res 
        
  