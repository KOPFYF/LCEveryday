class Solution(object):    
    def subarraySum(self, nums, k):
    	# time O(n), space O(n)
    	# init dict[0] = 1 for case like k - 0 = k, it means prefix sum = 0 is still a solution without picking anything
        count, cur, res = {0: 1}, 0, 0 
        for v in nums:
            cur += v # prefix sum
            res += count.get(cur - k, 0)
            count[cur] = count.get(cur, 0) + 1
        return res