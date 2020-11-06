class Solution {
    public int strangePrinter(String s) {
        // bottom up DP, time O(n^3) space O(n^2)
        int n = s.length();
        if (n == 0) return 0;
        
        int[][] dp = new int[n + 1][n];
        
        // base case
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        
        for (int d = 1; d < n; d++) {
            for (int i = 0; i + d < n; i++) {
                int j = i + d;
                dp[i][j] = dp[i + 1][j] + 1; // worst case, if s[i] not equals to any char in s[i+1:j]
                for (int k = i + 1; k <= j; k++) {
                    // 0 <= i < k <= j < n
                    if (s.charAt(i) == s.charAt(k)) {
                        // check start, if any s[k] == s[i], optimal print must be in one of them
                        dp[i][j] = Math.min(dp[i][j], dp[i][k - 1] + dp[k + 1][j]);
                    }
                }               
            }
        }
        
        return dp[0][n - 1];
    }
}