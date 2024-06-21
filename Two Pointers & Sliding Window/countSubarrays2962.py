class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Time O(n), Space O(1)
        maxnum = max(nums)
        i, j, n = 0, 0, len(nums)
        res, cnt = 0, 0

        while j < n:
            # grow right bound
            cnt += (nums[j] == maxnum)
            while cnt >= k: # reserve one slot for left index
                # shrink left bound
                cnt -= (nums[i] == maxnum)
                i += 1   
                
            # Update res by adding the value of i to account 
            # for all valid subarrays ending at index j
            res += i
            j += 1
 
        return res