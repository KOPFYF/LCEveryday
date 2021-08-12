class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        stack = [] # monotonically increasing stack
        
        for i in range(n+1):
            
            while stack and (i == n or nums[stack[-1]] >= nums[i]):
                # previous index with larger value needs to be poped out
                j = stack.pop()
                k = i - 1
                
                if stack:
                    k = k - stack[-1] + 1
                
                # k is the exact length of the subarray where you find the minimum value
                res[k] = max(res[k], nums[j])
                
            stack.append(i)
        
        # result of shorter subarray must be larger than that of longer subarray, so we add up all number backwards.
		# As a result res[0] will become the summation of the whole array.
        for i in range(n - 1, 0, -1):
            res[i - 1] = max(res[i - 1], res[i])
            
        return res