class Solution {
	public int coinChange(int[] coins, int amount) {
		if (amount < 1) return 0;
		int[] dp = new int[amount + 1];

		// top-down 1 dim dp
		// state machine: dp[amt] = min(dp[amt - coin] + 1)
		for (int i = 1; i <= amount; i++) {
			int min = -1;
			for (int coin: coins) {
				if (i - coin >= 0 && dp[i - coin] != -1) {
					int temp = dp[i - coin] + 1;
					// 2 cases to update min
					// either it's first time to see min = -1
					// or we have some smaller temp
                    if (min < 0 || temp < min) min = temp;
				}
			}
			dp[i] = min; // it could be -1
		}
		return dp[amount];

	}
}