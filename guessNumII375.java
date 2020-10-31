class Solution {
     /*
        dp[i][j] means pick one number from [i,j]，what's the min cost?
        State Machine：
        dp[i][j] = min(i + dp[i + 1][j], // pick i
                        ...
                       k + max(dp[i][k - 1], dp[k + 1][j]),  (k from i + 1 to j - 1) // pick k
                        ...
                       j + dp[i][j - 1] // pick j
                      )
        return: dp[1][n]
        time: O(n^3) 15 ms space: O(n^2) 38.2 MB
    */
    public int getMoneyAmount(int n) {
        if (n == 1) return 0;
        
        int[][] dp = new int[n + 1][n + 1];
        // base case, for(int i = 1; i <= n; i++) dp[i][i] = 0;
        // for (int j = 2; j <= n; j++) {
        //     for (int i = j - 1; i > 0; i--) {
        for (int i = n - 1; i > 0; i--) {
            for (int j = i + 1; j <= n; j++) {
                int a = Math.min(i + dp[i + 1][j], j + dp[i][j - 1]); // 2 ends
                int b = Integer.MAX_VALUE;
                for (int k = i + 1; k <= j - 1; k++) {
                    int tmp = k + Math.max(dp[i][k - 1], dp[k + 1][j]);
                    b = Math.min(b, tmp);
                }
                dp[i][j] = Math.min(a, b);
            }
        }
        return dp[1][n];
    }
}