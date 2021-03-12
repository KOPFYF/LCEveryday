class Solution:
    def myPow(self, x: float, n: int) -> float:
        # iteration
        if n < 0:
            n = -n
            x = 1/x
            
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        
        return res
    
        # soln 1, failed on OverflowError: (34, 'Numerical result out of range')
        # 2.00000
        # -2147483648
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        elif n == 0:
            return 1
        else:
            if n & 1: # odd
                return self.myPow(x ** 2, n // 2) * x
            else:
                return self.myPow(x ** 2, n // 2)
            
        # soln 2
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        elif n == 0:
            return 1
        else:
            if n & 1: # odd
                return self.myPow(x, n // 2) ** 2 * x
            else:
                return self.myPow(x, n // 2) ** 2
            