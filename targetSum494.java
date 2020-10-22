class Solution {
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