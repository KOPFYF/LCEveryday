/* 
This question eaquals to partition an array into 2 subsets whose difference is minimal
(1) S1 + S2 = S
(2) S1 - S2 = diff
==> -> diff = S - 2 * S2 ==> minimize diff equals to maximize S2
dp[i][j] means from stone 0 to stone i, we could fit them into a bag size of j
i ranges from {1..n}
j ranges from (sum of all elements) {1..n}
*/
class Solution1 {

    public int lastStoneWeightII(int[] stones) {
        int n = stones.length, sum = 0;
        for (int stone : stones) sum += stone;
        int target = sum / 2;
        
        int[][] dp = new int[n + 1][target + 1];
        int S2 = 0; // need to max S2 so to min diff
        
        for(int i = 0; i < dp.length; i++)
            dp[i][0] = 1; // every i should have an empty subgroup with zero sum
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= target; j++) {
                if(dp[i-1][j] == 1 || (j >= stones[i-1] && dp[i-1][j-stones[i-1]] == 1)){
                    // case 1: stone 0 to stone i-1, if it is a fit, then add stone i will also fit
                    // case 2: current bag size j > curr stone && dp[i-1][j - stones[i-1]]
                    dp[i][j] = 1;
                    S2 = Math.max(S2, j);   
                }
                
            }
        }
        return sum - 2 * S2; // remember S - 2 * S2 = diff
    }
}

class Solution2 {
    public int lastStoneWeightII(int[] stones) {
        int sum = 0;
        for (int stone : stones) sum += stone;
        int target = sum / 2;

        boolean[] dp = new boolean[target + 1];
        dp[0] = true; // The first achievable dp spot, but not a solution in this problem
        int minDiff = Integer.MAX_VALUE;
        for(int stone : stones) {
            for (int j = target; j >= stone; j--) {
                dp[j] |= dp[j-stone];
                if (dp[j]) {
                    minDiff = Math.min(minDiff, sum - 2 * j);
                }
            }
        }
        return minDiff;
    }
}