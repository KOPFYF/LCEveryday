class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        if (s == null || n == 0) return 0;
        
        int[] dp = new int[n + 1];
        dp[0] = 1; // empty string
        dp[1] = s.charAt(0) != '0' ? 1 : 0;
        
        for (int i = 2; i < n+1; i++) {
            int fst = Integer.valueOf(s.substring(i-1, i));
            int snd = Integer.valueOf(s.substring(i-2, i));
            
            if (fst >= 1 && fst <= 9) dp[i] += dp[i - 1];
            if (snd >= 10&& snd <=26) dp[i] += dp[i - 2];
        }
        
        return dp[n];
        
    }
}