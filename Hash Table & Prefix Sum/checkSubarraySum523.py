class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # presum + hashmap, O(n)/O(n)
        d = {}
        d[0] = -1 # index init as -1, cnt init as 1
        s = 0
        for i, num in enumerate(nums):
            s += num
            if k != 0: 
                s %= k
            if s in d: # find another same pattern
                if i - d[s] >= 2:
                    return True
            else:
                d[s] = i # record the pattern of the first appearance
        return False