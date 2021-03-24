class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:   # overflow case
            return 2**31 - 1

        sign = 1
        if (dividend > 0) ^ (divisor > 0):
            sign = -1

        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1): 
                multiple <<= 1
                temp <<= 1
            res += multiple
            dividend -= temp
        return res * sign