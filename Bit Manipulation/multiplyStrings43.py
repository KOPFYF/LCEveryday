class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        110(6) shift right
        111(7) shift left
        
        01110
        11100
       101010 = 2 ^ 5 + 2 ^ 3 + 2 ^ 1
        a 0b110
        a 0b11 (find a one)
        b 0b1110 (shift b to the left one step)
        a 0b1 ( find another one)
        b 0b11100 (shift b left again)
        '''
        a = int(num1)
        b = int(num2)
        res = 0
        k = 0
        while a:
            # print('a', bin(a))
            if a & 1: # fina a one
                res += b << k
                # print('b', bin(b << k))
            a >>= 1
            k += 1
        return str(res)