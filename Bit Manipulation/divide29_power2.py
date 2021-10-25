class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        '''
        truncate toward zero
        2**31 = 2147483648
        −2**31 / (-1) will overflow
        
        '''
        # O(logn) / O(1)
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1 # capped
        
        sign = (dividend > 0) ^ (divisor < 0)
        # print(sign) # True if they have the same sign
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        
        while dividend >= divisor:
            # dividend = divisor * (2^1 + 2^5 + 2^7 + ... etc)
            tmp = divisor
            i = 1
            while dividend >= tmp:
                dividend -= tmp
                res += i
                i <<= 1
                tmp <<= 1 # tmp = divisor * 2 ^ n, 2^n = i
        
        if not sign:
            res = -res  
        return res
            
            
            