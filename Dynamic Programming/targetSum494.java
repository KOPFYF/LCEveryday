class Solution1 {
    // dfs, no memo, 439 ms, time O(2^n), space O(n^2)
    int res = 0;
    public int findTargetSumWays(int[] nums, int S) {
        if (nums.length == 0) return 0;
        dfs(nums, S, 0);
        return res;
    }
    
    private void dfs(int[] nums, int target, int pos) {
        if (pos == nums.length) {
            if (target == 0) {
                res++;
            }
            return;
        }
        dfs(nums, target - nums[pos], pos + 1);
        dfs(nums, target + nums[pos], pos + 1);
    }
}

class Solution2 {
    // 2 dim DP (0/1 knapsack) Time: O(n^2), Space: O(n^2), 16 ms, 38.7 MB
    // dp[i][j] represents number of possible ways to reach sum j by using first ith items
    public int findTargetSumWays(int[] nums, int S) {
        int n = nums.length, sum = 0;
        
        if (n == 0) return 0;
        for (int num: nums) sum += num;
        if (S < -sum || S > sum) return 0;
        
        int[][] dp = new int[n + 1][2 * sum + 1];
        dp[0][0 + sum] = 1; // 0 + sum is center, and it means 0, 0 means -sum, s*sum means sum  
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= 2 * sum; j++) {
                if (j + nums[i - 1] <= 2 * sum) {
                    dp[i][j] += dp[i - 1][j + nums[i - 1]];
                }
                if (j - nums[i - 1] >= 0) {
                    dp[i][j] += dp[i - 1][j - nums[i - 1]];
                }
            }
        }
        return dp[n][sum + S]; //consider offset by -sum
    }
}

class Solution3 {
    // 1 dim DP (0/1 knapsack) Time: O(n^2), Space: O(n), 16 ms, 38.7 MB
    // dp[j] represents number of possible ways to reach sum j 
    public int findTargetSumWays(int[] nums, int S) {
        int n = nums.length, sum = 0;
        
        if (n == 0) return 0;
        for (int num: nums) sum += num;
        if (S < -sum || S > sum) return 0;
        
        int[] dp = new int[2 * sum + 1];
        dp[0 + sum] = 1; // 0 + sum is center, and it means 0, 0 means -sum, s*sum means sum  
        for (int i = 1; i <= n; i++) {
            int[] nxt = new int[2 * sum + 1];
            for (int j = 0; j <= 2 * sum; j++) {
                if (j + nums[i - 1] <= 2 * sum) {
                    nxt[j + nums[i - 1]] += dp[j];
                }
                if (j - nums[i - 1] >= 0) {
                    nxt[j - nums[i - 1]] += dp[j];
                }
            }
            dp = nxt;
        }
        return dp[sum + S]; //consider offset by -sum
    }
}

