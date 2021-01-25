class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # DP, `dp[0]` maintain the `k smallest array sum` in `mat[:1]`.
        # It is possible that `k > len(mat[0])`. 
        # If so, `dp[0]` can only maintain the `len(mat[0]) smallest array sum` in `mat[:1]` at most.
        m, n = len(mat), len(mat[0])
        dp = mat[0][:min(k, n)]
        # print(dp)
        for row in mat[1:]:
            tmp = []
            # Compute the cross product between `dp[i-1]` and `mat[i]` for new pairs
            for i in dp:
                for j in row:
                    tmp += [i+j]
            dp = sorted(tmp)[:min(k, len(tmp))]
            # print(dp, len(dp)) # len(dp) = k in the loop
        return dp[-1]
        