class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        // idea is to fix the first num, then reduce it to 2 sum
        // O(n^2)
        for (int i = 0; i + 2 < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i-1]) 
                continue; //dedup
            
            int j = i + 1, k = nums.length - 1; // 2 pointers
            int target = -nums[i];
            
            // reduce to 2 sum
            while (j < k) {
                if (nums[j] + nums[k] == target) {
                    res.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j++; 
                    k--;
                    while (j < k && nums[j] == nums[j - 1]) j++;  // skip same result
                    while (j < k && nums[k] == nums[k + 1]) k--;  // skip same result
                } 
                else if (nums[j] + nums[k] > target) 
                    k--;
                else 
                    j++;
            }
        }
        return res;
    }
}