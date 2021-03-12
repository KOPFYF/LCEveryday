class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0 : -1}
        s, res = 0, 0
        for i, num in enumerate(nums):
            # if num:
            #     s += 1
            # else:
            #     s -= 1
            s += (2 * num - 1)
            if s in d:
                res = max(res, i - d[s])
            else:
                d[s] = i
        return res