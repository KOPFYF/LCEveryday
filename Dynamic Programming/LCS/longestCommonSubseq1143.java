class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        // Bottom Up DP, time O(n1 * n2), space O(n1 * n2)
        // dp[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j]
        int n1 = text1.length();
        int n2 = text2.length();
        
        int[][] dp = new int[n1 + 1][n2 + 1];
        
        for (int i = 0; i < n1; i++) {
            for (int j = 0; j < n2; j++) {
                if (text1.charAt(i) == text2.charAt(j)) {
                    dp[i + 1][j + 1] = 1 + dp[i][j];
                }
                else {
                    dp[i + 1][j + 1] = Math.max(dp[i + 1][j], dp[i][j + 1]);
                }
            }
        }
        
        return dp[n1][n2];  
    }
}