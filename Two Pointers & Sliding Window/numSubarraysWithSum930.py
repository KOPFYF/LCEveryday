class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound):
            # only care about whether each element is less than
            # count(B) is the number of subarrays that have all elements less than or equal to B
            res, cur = 0, 0
            for num in nums:
                if num <= bound:
                    cur += 1
                else:
                    cur = 0
                res += cur
            return res
        
        '''
        [2,1,4,3], left = 2, right = 3
        count(2) [2] [2,1], [1]
        count(1) [1]
        count(3) [2], [2,1], [1], [3]
        
        '''
        return count(right) - count(left - 1)

class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        # Sliding window
        i = cnt = res = 0
        for j in range(len(A)):
            cnt += A[j]
            while i < j and cnt > S:
                cnt -= A[i]
                i += 1
            if cnt < S: continue
            if cnt == S: res += 1
            k = i 
            # temp pointer deal with left zero
            while k < j and not A[k]:
                k += 1
                res += 1
        return res