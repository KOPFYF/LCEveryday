'''
For every index do a binary search to get the possible right end of the window and calculate the possible answer.

Store the original length, n = len(nums).
Firstly, make elements in nums unique and sort nums array.
Try elements in nums as the start of the continuous array, let say start.
Elements in the continuous array must in range [start, end], where end = n - start + 1.
Binary search to find the index of the right insert position of end in nums, let say idx.
Then we can calculate the number of unique numbers in range [start, end] by uniqueLen = n - idx.
The cost to make coninuous array is cost = n - uniqueLen.
We update the best answer so far, ans = min(ans, cost)
Then return the best ans we have.
'''
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # binart search O(NlogN)/O(N)
        n = len(nums)
        nums = sorted(set(nums)) # Make `nums` as unique numbers and sort `nums`.
        
        res = n
        for i, start in enumerate(nums):
            # fix the lower end, then fix the whole range, finally get the cost out of range
            end = start + n - 1 # We expect elements of continuous array must in range [start..end]
            idx = bisect.bisect_right(nums, end) # Find right insert position
            uniqueLen = idx - i
            res = min(res, n - uniqueLen)
            # print(i, start, end, idx, uniqueLen, n - uniqueLen)
        return res