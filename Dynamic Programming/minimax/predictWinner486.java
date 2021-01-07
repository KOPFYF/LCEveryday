class Solution1 {
    public boolean PredictTheWinner(int[] nums) {
        // DFS + memo, time: O(n) 0ms 100%, space: O(n^2)
        // memo[i][j], as the 1st picker, he can get max points in nums[i:j+1]
        // + if 1st picks, - if 2nd picks(当前自己的选择得分为正，对手的选择得分为负)
        int n = nums.length;
        int[][] memo = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            Arrays.fill(memo[i], Integer.MIN_VALUE);
        }
        return dfs(nums, 0, n - 1, memo) >= 0;
    }
    
    private int dfs(int[] nums, int i, int j, int[][] memo) {
        if (i > j) return 0;
        
        if (memo[i][j] != Integer.MIN_VALUE) return memo[i][j];
        
        int l = nums[i] - dfs(nums, i + 1, j, memo); // A pick nums[i], and B max nums[i+1..j]
        int r = nums[j] - dfs(nums, i, j - 1, memo); // A pick nums[j], and B max nums[i..j-1]
        memo[i][j] = Math.max(l, r);
        return memo[i][j];
    }
}

class Solution2 {
    public boolean PredictTheWinner(int[] nums) {
        // DP, time O(n), space O(n^2), 0ms
        // dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        int n = nums.length;
        int[][] dp = new int[n][n];
        
        for (int i = 0; i < n; i++) dp[i][i] = nums[i]; // base
        
        // i depends on i + 1(future), j depends on j - 1(former), and i < j
        // so we start from right-down corner and then to left-up!!, aka i--, j++
        for (int i = n - 2; i >= 0 ; i--) {
            for (int j = i + 1; j < n; j ++) {
                dp[i][j] = Math.max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);
            }
        }
        
        return dp[0][n - 1] >= 0;
    }
}

class Solution3 {
    public boolean PredictTheWinner(int[] nums) {
        // DP, time O(n), space O(n^2)
        // dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        int n = nums.length;
        int[][] dp = new int[n][n];
        
        for (int i = 0; i < n; i++) dp[i][i] = nums[i]; // base
        
        // i depends on i + 1(future), j depends on j - 1(former), and i < j
        // another index loop from left-up to right-down, still i--, j++
        for (int j = 1; j < n; j++ ) {
            for (int i = j - 1; i >= 0; i--) {
                dp[i][j] = Math.max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);
            }
        }
        
        return dp[0][n - 1] >= 0;
    }
}