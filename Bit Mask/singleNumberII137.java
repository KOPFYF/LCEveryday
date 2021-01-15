class Solution {
    public int singleNumber(int[] nums) {
        int res = 0;
        int[] map = new int[32];
        // save to map
        for (int i = 0; i < nums.length; i++)
            saveToMap(nums[i], map);
        // remove num appears 3 times
        for (int i = 0; i < 32; i++)
            map[i] = map[i] % 3;
        // the remaining is only one num
        for (int i = 0; i < 32; i++)
            res |= map[i] << i;
        return res;
    }
    
    private void saveToMap(int num, int[] map) {
        for (int i = 0; i < 32; i++)
            map[i] += (num >> i) & 1;
    }
}