class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # get / isolate the rightmost 1-bit : x & (-x)
        # turn off (= set to 0) the rightmost 1-bit : x & (x - 1)
        
        # soln 1, get rightmost 1-bit, O(1)
        if n == 0:
            return False
        return n & (-n) == n
    
        # soln 2, turn off the rightmost 1-bit, O(1)
        if n == 0:
            return False
        return n & (n - 1) == 0
        
        
        # O(logn)
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1