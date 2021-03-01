class Solution:
    def diagonalSort(self, A: List[List[int]]) -> List[List[int]]:
        # sort, O(mn + dlogd)
        # A[i][j] on the same diagonal have same value of i - j
        m, n = len(A), len(A[0])
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[i - j].append(A[i][j])
        
        for k in d:
            d[k].sort(reverse=True) # reverse sort, LIFO
            
        for i in range(m):
            for j in range(n):
                A[i][j] = d[i - j].pop() # small i, j will come first
        return A