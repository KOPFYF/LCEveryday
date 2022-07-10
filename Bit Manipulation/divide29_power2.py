class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # O(32)
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        sign = (dividend > 0) == (divisor > 0) # if True, pos
        dividend, divisor = abs(dividend), abs(divisor)
        
        tmp, res = 0, 0
        for i in range(31, -1, -1):
            if tmp + (divisor << i) <= dividend:
                tmp += divisor << i
                res += 1 << i
    
        # res = 0
        # while dividend >= divisor:
        #     tmp, i = divisor, 1
        #     while dividend >= tmp:
        #         dividend -= tmp
        #         res += i
        #         i <<= 1
        #         tmp <<= 1
        
        if sign:
            return res
        else:
            return -res


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        '''
        truncate toward zero
        2**31 = 2147483648
        −2**31 / (-1) will overflow

        93706 / 157

        tmp     i    dividend
        (80384, 512,  13479)
        (10048, 64,   3588)
        (2512,  16,   1233)
        (1256,  8,     134)

        
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
            print(tmp, i, dividend)
        
        if not sign:
            res = -res  
        return res
            
            
            