class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # sliding window does not work cuz neg elements
        d = defaultdict(int)
        d[0] = 1
        s, cnt = 0, 0
        for num in nums:
            s += num
            if s - k in d:
                cnt += d[s - k]
            d[s] += 1 # no matter if condition, we update the hashmap
        return cnt
        
        d = {0 : 1}
        s, cnt = 0, 0
        for num in nums:
            s += num
            if s - k in d:
                cnt += d[s - k]
            d[s] = d.get(s, 0) + 1
        return cnt

class Solution0(object):    
    def subarraySum(self, nums, k):
    	# time O(n), space O(n)
    	# init dict[0] = 1 for case like k - 0 = k, it means prefix sum = 0 is still a solution without picking anything
        count, cur, res = {0: 1}, 0, 0 
        for v in nums:
            cur += v # prefix sum
            res += count.get(cur - k, 0)
            count[cur] = count.get(cur, 0) + 1
        return res