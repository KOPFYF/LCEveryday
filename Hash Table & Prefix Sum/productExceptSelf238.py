class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, post = [1] * n, [1] * n
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]
            
        for j in range(n - 1, 0, -1):
            # j from n - 1 to 1
            post[j - 1] = post[j] * nums[j ]
            
        # print(pre, post)
        res = [1] * n
        for i in range(n):
            res[i] = pre[i] * post[i]
        return res