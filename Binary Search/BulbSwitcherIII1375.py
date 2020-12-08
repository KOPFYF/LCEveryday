class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        # right is the number of the right most lighted bulb.
        right = res = 0
        for i, a in enumerate(light, 1):
            right = max(right, a)
            res += right == i
        return res