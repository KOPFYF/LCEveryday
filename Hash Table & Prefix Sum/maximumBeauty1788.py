'''
Length of flowers array is 10^5 => the algorithm needs to be O(n) or O(nlogn)
There is always a valid solution so don't worry about edge cases (e.g no solution)
In order to compute the max sum, we only need to include the positive numbers between the first and the last
First and last might be negative, so we have to take this into account when we compute the maxsum
Everything can be done in one traversal:
use a list for the positive prefix sums
use a hashtable to store the first position of every flower

'''

class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        # prefix sum O(n) / O(n)
        presum = [0]
        idxs = {}
        res = -float('inf')
        
        for i, flower in enumerate(flowers):
            pval = flower if flower >= 0 else 0
            nval = flower if flower < 0 else 0
            presum.append(presum[-1] + pval) # greedyly count positive only
            if flower not in idxs:
                # record the first position of each flower
                idxs[flower] = i 
            else:
                # given that negative numbers are not part of the prefix sum,
                # we need to include them if they are the first / last items
                first_pos = idxs[flower]
                cur = 2 * nval + presum[i + 1] - presum[first_pos]
                res = max(cur, res)
        return res