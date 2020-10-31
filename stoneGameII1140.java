class Solution {
    // dp[i][j] is the maximum number of stones Alex can get when starting at index i with M = j
    // choose an optimal X to minimize the number of stones Lee can get when starting at index (i + X) with M = max(X,j)
    // aka, dp[i][j] = max(sufsum[i] - dp[i + X][max(j, X)]) where 1<= X <= 2*j;
    // Time: O(n^3) 3ms, Space: O(n^2) 36.4 MB 
    public int stoneGameII(int[] piles) {
        int n = piles.length;
        int[] prefixSum = new int[n + 1]; // Sum from i to the end
        for (int i = n - 1; i >= 0; i--) {
            prefixSum[i] = prefixSum[i + 1] + piles[i];
        }
        
        int[][] dp = new int[n][n + 1];
        for (int i = n - 1; i >= 0; i--) {
            for (int M = 1; M <= n; M++) {
                if (i + 2 * M >= n) {
                    dp[i][M] = prefixSum[i]; // index overflow, Alex can take all
                    continue; 
                }
                for (int x = 1; x <= 2 * M; x++) {
                    // Alex take i to i + x, and make dp[i + x][max(M, x)] minimum
                    dp[i][M] = Math.max(dp[i][M], prefixSum[i] - dp[i + x][Math.max(M, x)]);
                }
            }
        }
        return dp[0][1];
        
    }
}

class Solution2 {
    // DFS + memo
    // Time: O(n^2)? 0ms, Space: O(n^2) 36.3 MB 
    public int stoneGameII(int[] piles) {
        int n = piles.length;
        int[] presum =  Arrays.copyOf(piles, n);
        for (int i = presum.length - 2; i >= 0; i--) 
            presum[i] += presum[i + 1];
        return dfs(presum, 1, 0, new int[n][n]);
    }
    
    private int dfs(int[] presum, int m, int p, int[][] memo) {
        if (p + 2 * m >= presum.length) { 
            return presum[p]; // last player takes all
        }

        if (memo[p][m] > 0) return memo[p][m];
        int res = 0, take = 0;
        for (int i = 1; i <= 2 * m; i++) {
            // current take
            take = presum[p] - presum[p + i];
            // take max of current + what lefts from other player max take
            res = Math.max(res, take + presum[p + i] - dfs(presum, Math.max(i, m), p + i, memo));
        }
        memo[p][m] = res;
        return res;

    }
}