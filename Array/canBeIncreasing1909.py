'''
    int cnt = 0;
    for (int i = 1; i < nums.size() && cnt < 2; ++i) {
        if (nums[i - 1] >= nums[i]) {
            ++cnt;
            if (i > 1 && nums[i - 2] >= nums[i])
                nums[i] = nums[i - 1];
        }
    }
    return cnt < 2;

    When we find a drop, we check if the current number nums[i] is greater than the number before the previous one nums[i - 2].

If so, the number nums[i - 1] needs to be removed.
Otherwise, the current number needs to be removed (nums[i]).
For simplicity, I just assign the previous value to the current number (nums[i] = nums[i - 1]).
And, of course, we return false if we find a second drop.

'''

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(1, len(nums)):
            if cnt >= 2:
                return False
            if nums[i - 1] >= nums[i]:
                cnt += 1
                # the current number needs to be removed (nums[i])
                if i > 1 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]
        return cnt < 2
        
        
        def check(nums):
            for a, b in zip(nums, nums[1:]):
                if b <= a:
                    return False
            return True
        
        for i in range(len(nums)):
            new = nums[:i] + nums[i+1:]
            if check(new):
                return True
        return False
                