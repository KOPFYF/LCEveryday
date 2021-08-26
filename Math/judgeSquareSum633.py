class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        '''
        0 <= c <= 2^31 - 1
        2^31 = 2,147,483,648 ~= 2 * 10^9
        Time complexity : O(c^0.5 logc). We iterate over O(c^0.5) values for choosing a. For every a             chosen, finding square root of c - a^2 takes O(logc) time in the worst case.
        Space complexity : O(1)O(1). Constant extra space is used.
        '''
        for num in range(int(sqrt(c)) + 1):
            res = c - num * num
            if sqrt(res) == int(sqrt(res)):
                return True
        return False