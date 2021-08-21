'''

soln 1:
If we create the first square matrix, the big matrix will just be the copies of this one. (translation copies)
The value of each location in the square matrix will appear at multiple locations in the big matrix, count them.
Then assign the ones in the square matrix with more occurances with 1.

soln 2: pq, https://youtu.be/FjIao84fqLg
'''
class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        # greedy, uniform distribution
        res = []
        for i in range(sideLength):
            for j in range(sideLength):
                res += [((width - i - 1) // sideLength + 1) * ((height - j - 1) // sideLength + 1)]
                # print(i, j, res)
        res = sorted(res, reverse = True)
        # print(res)   
        
        return sum(res[:maxOnes])