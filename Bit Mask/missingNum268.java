class Solution {
    public int missingNumber(int[] nums) {
        // XOR loop twice
        int miss = 0;
        for (int num : nums)
            miss ^= num;
        for (int i = 1; i <= nums.length; i++)
            miss ^= i;
        return miss;
    }
}