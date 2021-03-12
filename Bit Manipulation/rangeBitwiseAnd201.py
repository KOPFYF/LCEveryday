class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        '''
        Soln 1
        the bitwise and of the range is keeping the common bits of m and n from left to right 
        until the first bit that they are different, padding zeros for the rest.
        m: 11111|0101011
        n: 11111|0110110
        For example, for number 26 to 30
        Their binary form are:
        11010
        11011
        11100　　
        11101　　
        11110

        Because we are trying to find bitwise AND, so if any bit there are at least one 0 and one 1, it always 0. In this case, it is 11000.
        So we are go to cut all these bit that they are different. In this case we cut the right 3 bit.

        '''
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i
    
        # soln 2
        # Bitwise-AND of any two numbers will always produce a number less than or equal to the smaller number.
        while n > m: 
            n = n & (n-1) # jump down
        return m & n