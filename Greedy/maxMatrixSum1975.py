'''
Hints:
Try to use the operation so that each row has only one negative number.
If you have only one negative element you cannot convert it to positive.

Recognize that if there is an even amount of negative numbers, you can eliminate all the negatives signs in the following fashion:

If there is a pair of adjacent negative numbers, just remove both negative signs
If the remaining negative numbers are separated from each other, just swap their negative signs with the adjacent positive number until they are adjacent to each other, and then you can remove 2 negative signs at a time
If there is an odd amount of negative sign, there will be a negative sign in the end, and we can move that negative sign to the smallest number in the matrix (by swapping as above)

So, if the number of negative signs is even, the answer is the sum of the absolute value of all elements. If it is odd, we will have to minus 2 times the number with smallest absolute value (for we have to change + sign to -) to get the answer
'''
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # greedy, O(n^2)
        res, n, neg_cnt, minn = 0, len(matrix), 0, float('inf')
        for i in range(n):
            for j in range(n):
                res += abs(matrix[i][j])
                neg_cnt += (matrix[i][j] < 0)
                # at most 1 neg will be left, choose the smallest one
                minn = min(minn, abs(matrix[i][j])) 

        return res - 2 * minn if neg_cnt & 1 else res