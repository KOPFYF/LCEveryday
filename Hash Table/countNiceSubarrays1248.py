class Solution1(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Solution 1: sliding window with at most helper.
        def atmost(nums, k):
            res = 0
            i = 0
            n = len(nums)
            for j in range(n):
                k -= nums[j] % 2
                while k < 0:
                    k += nums[i] % 2
                    i += 1
                res += j - i + 1    
                
            return res
        
        return atmost(nums, k) - atmost(nums, k - 1)


class Solution2(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Solution 2: hashmap
        # Transform the input array into binary, then it's Subarray Sum Equals K
        # Just keep count of the current odd number.
        # Look in the dictionary if we can find (currendOds - k), 
        # if it exisits that means I can get an subarray with k odds.
        # Also keep count of number of different types of odds too,
        # because for K =1 , [2,2,1] is a valid list, so does, [2,1] and [1].
        d = {0:1}
        curodd = res = 0
        for j, num in enumerate(nums):
            if num % 2:
                curodd += 1
 
            res += d.get(curodd - k, 0)
            d[curodd] = d.get(curodd, 0) + 1
                
        return res  