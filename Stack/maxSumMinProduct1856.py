class Solution0:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n, res, mod = len(nums), 0, 10**9 + 7
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]
        stack = []
        for i, h in enumerate(nums + [0]): # +[0] critial
            start = i
            while stack and h <= stack[-1][1]: # mono inc
                start, minh = stack.pop()
                res = max(res, minh * (presum[i] - presum[start]))
                # print(start, i, minh, res)
            stack.append((start, h))
        return res % mod

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n, res, mod = len(nums), 0, 10**9 + 7
        
        ls, s1 = [0], [(nums[0], 0)] # count of nums bigger on the left
        for i in range(1, n):
            cnt = 0
            while s1 and nums[i] <= s1[-1][0]:
                cnt += s1.pop()[1] + 1
            s1.append((nums[i], cnt))
            ls.append(cnt)
        # print(ls)
        
        rs, s2 = [0], [(nums[-1], 0)] # count of nums bigger on the right
        for j in range(n - 2, -1, -1):
            cnt = 0
            while s2 and nums[j] <= s2[-1][0]:
                cnt += s2.pop()[1] + 1
            s2.append((nums[j], cnt))
            rs.append(cnt)
        rs = rs[::-1]
        # print(rs)
        
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]
        
        for i, (num, l, r) in enumerate(zip(nums, ls, rs)):
            res = max(res, num * (presum[i + r + 1] -  presum[i - l])) % mod
        
        return res % mod