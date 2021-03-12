class Solution {
    public int[] singleNumber(int[] nums) {
        // how to split?
        // binary code, inverse code, complement code
        // 正数： 补码=反码=原码
        // 负数： 补码=反码+1
        int xor = 0;
        for (int i = 0; i < nums.length; i++) xor ^= nums[i];
        int lastDigit = xor & (-xor); 
        // to diffreciate 2 nums,  xor & (~xor + 1) also ok
        int group1 = 0, group2 = 0;
        for (int i = 0; i < nums.length; i++) {
            if ((lastDigit & nums[i]) == 0)
                group1 ^= nums[i];
            else
                group2 ^= nums[i];
        }
        return new int[]{group1, group2};
    }
}