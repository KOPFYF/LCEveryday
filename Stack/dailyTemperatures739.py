class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res, stack = [0] * len(T), []
        for i, temp in enumerate(T):
            while stack and T[stack[-1]] < temp:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res