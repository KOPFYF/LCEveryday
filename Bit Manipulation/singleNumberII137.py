class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # soln 1, O(n)
        # 1. adding "val" to the "set" if "val" is not in the "set" => A^0 = A
        # 2. removing "val" from the "set" if "val" is already in the "set" => A^A = 0
        one, two = 0, 0
        for num in nums:
            one = (one ^ num) & ~two
            two = (two ^ num) & ~one
        return one    
            
        # soln 2, O(32n)
        # Iterate over all possible 32 bits and for each num check if this num has non-zero bit on position i with num & (1<<i) == (1<<i) formula.
        # We evaluate this sum modulo 3. Note, that in the end for each bit we can have either 0 or 1 and never 2.
        # Next, update our answer single with evaluated bit.
        # Finally, we need to deal with overflow cases in python: maximum value for int32 is 2^31 - 1, so if we get number more than this value we have negative answer in fact.
        single = 0
        for i in range(32):
            count = 0
            for num in nums:
                if (num >> i) & 1: # count 1 for all num at current bit
                    count += 1
            single |= (count % 3) << i
            
        return single if single < (1<<31) else single - (1<<32) 