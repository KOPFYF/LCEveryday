class Solution:
    def minimumDeletions(self, A: List[int]) -> int:
        '''
        
        Find index i of the minimum
        Find index j of the maximum

        To remove element A[i],
        we can remove i + 1 elements from front,
        or we can remove n - i elements from back.
        '''
        i, j, n = A.index(min(A)), A.index(max(A)), len(A)
        return min(max(i + 1, j + 1), max(n - i, n - j), i + 1 + n - j, j + 1 + n - i)