'''
Sort the input array A
Sliding window prolem actually,
the key is to find out the valid condition:
k + sum >= size * max
which is
k + sum >= (j - i + 1) * A[j]

     Number of operations needed for all elements in the window [startIndex, endIndex] to hit A[endIndex]
     Example:
     Consider arr with [1, 2, 3, 4] with startIndex = 0; endIndex = 3: i.e If 1, 2, 3 wants to become 4.
     Number of operations needed
     = (4-1)+(4-2)+(4-3)+(4-4) = 6.
     =  4 + 4 + 4 + 4 - (1 + 2 + 3 + 4)
     = 4 * 4 - (1 + 2 + 3 + 4)
     = (number of elements) * ElementToReach - sum of elements in the window

'''
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        i, res, s = 0, 1, 0
        nums.sort()
        for j in range(len(nums)):
            s += nums[j]
            while s + k  < nums[j] * (j - i + 1):
                s -= nums[i]
                i += 1
            res = max(res, j - i + 1)
        return res
            