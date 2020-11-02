// Given a list of numbers, multiply each number with 1 or 0 or -1, make the sum of all numbers to 0. 
// Find a combination which has the largest sum of all positive numbers.
class Solution1 {
    public int tallestBillboard(int[] rods) {
        // HashMap DP, 250 ms
        // https://leetcode.com/problems/tallest-billboard/discuss/219700/Python-DP-clean-solution(1D)
        // https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/956.Tallest-Billboard
        // key : sum, aka the diff between left & right, value : max sum of height
        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(0, 0);
        for (int rod : rods) {
            Map<Integer, Integer> nxt = new HashMap<>();
            for (int s : dp.keySet()) {
                // multiply by 1, put rod on the left, nxt[s + rod] = max(dp[s] + rod, nxt[s + rod])
                nxt.put(s + rod, Math.max(rod + dp.get(s), nxt.getOrDefault(s + rod, 0)));
                // multiply by 0, dont pick such rod, nxt[s] = max(dp[s], nxt[s])
                nxt.put(s, Math.max(dp.get(s), nxt.getOrDefault(s, 0)));
                // multiply by -1, put rod on the right, nxt[s - rod] = max(dp[s], nxt[s - rod])
                nxt.put(s - rod, Math.max(dp.get(s), nxt.getOrDefault(s - rod, 0)));
            }
            dp = nxt;
        }
        return dp.get(0);
    }
}


class Solution2 {
    // 21 ms https://leetcode.com/problems/tallest-billboard/discuss/203181/JavaC%2B%2BPython-DP-min(O(SN2)-O(3N2-*-N)
    public int tallestBillboard(int[] rods) {
        int[] dp = new int[5001]; // diff between tall & short, 0 <= d <= 5000
        for (int d = 1; d < 5001; d++) dp[d] = -5000;
        for(int rod: rods) {
            int[] temp = dp.clone();
            for(int i = 0; i + rod <= 5000; i++) {
                // put rod to the tall side
                dp[i + rod] = Math.max(dp[i + rod], temp[i]);
                // put rod to the short side
                if (i > rod) {
                    // put rod to the short side and rod < diff
                    dp[i - rod] = Math.max(dp[i - rod], temp[i] + rod);
                } else {
                    // put rod to the short side and rod >= diff
                    dp[rod - i] = Math.max(dp[rod - i], temp[i] + i);
                }
                // dp[Math.abs(i - rod)] = Math.max(dp[Math.abs(i - rod)], temp[i] + Math.min(rod, i));
            }
        }
        
        return dp[0];
    }
}