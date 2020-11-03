class Solution {
    public int minScoreTriangulation(int[] A) {
        // bottom up DP, dp[i][j] means the minimum score to triangulate A[i] ~ A[j]
        // Time O(n^3), Space O(n^2)
        // 0 <= i < k < j < n
        int n = A.length;
        int[][] dp = new int[n][n];
        for (int d = 2; d < n; d++) {
            for (int i = 0; i + d < n; i++) {
                int j = i + d;
                dp[i][j] = Integer.MAX_VALUE;
                for (int k = i + 1; k < j; k++) {
                    dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[j] * A[k]);
                }
            }
        }
        return dp[0][n - 1];
    }
}