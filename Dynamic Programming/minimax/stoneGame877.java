class Solution1 {
    public boolean stoneGame(int[] piles) {
        // dp[i][j] means max stones from [i, j], 0 <= i <= j <= n
        // dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        // Time O(n^2) 4 ms, Space O(n^2) 39.6 MB
        int n = piles.length;
        if (piles == null || n == 1) return true;
        
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            dp[i][i] = piles[i]; // base case
        }
        
        // bottom up
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                dp[i][j] = Math.max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1]);
            }
        }
        
        return dp[0][n-1] > 0;
    }
}

class Solution2 {
    public boolean stoneGame(int[] piles) {
        // dp[i][j] means max stones from [i, j], 0 <= i <= j <= n
        // dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        // Compress dp tp 1 dimension
        // Time O(n^2) 3 ms, Space O(n) 36.8 MB
        int n = piles.length;
        if (piles == null || n == 1) return true;
        
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = piles[i]; // base case
        }
        
        // bottom up
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                // dp[i][j] = Math.max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1]);
                // compress 
                dp[j] = Math.max(piles[i] - dp[j], piles[j] - dp[j-1]);
            }
        }
        
        return dp[n-1] > 0;
    }
}