'''
The goal is to keep track of:

Maximum So far and add it to the cur_cell and maintain maximum result
Here, max_so_far contains : A[i] + i
Original Given Formula : A[i] + A[j] + i - j

Break in two parts : A[i] + i and A[j] -j
Keep MAX_VALUE of first part among the elements seen so far
Add the current element to max_so_far and check the result is changing or not
Also, keep updating the max_so_far at each step
'''

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # dp, sell stocks
        # max(values[i] + values[j] + i - j) 
        # => max( (values[i] + i) + (values[j] - j) )
        max_so_far, res = a[0], 0
        # one loop since i < j
        for i in range(1, len(a)):
            res = max(res, max_so_far + a[i] - i)
            max_so_far = max(max_so_far, a[i] + i)
			
        return res