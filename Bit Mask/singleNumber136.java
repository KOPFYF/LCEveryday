class Solution {
    public int singleNumber(int[] nums) {
    	// bit mask space O(1)
    	// a ^ a = 0, b ^ 0 = b
        int res = 0;
        for (int num : nums) res ^= num;
        return res;
    }
}