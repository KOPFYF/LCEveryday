class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        
        carrier = 0
        res = ''
        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carrier += 1
            if b[i] == '1':
                carrier += 1
            if carrier % 2 == 1:
                res += '1'
            else:
                res += '0'
            
            carrier //= 2 # when it's 2, make it 1
        
        if carrier:
            res += '1'
        return res[::-1]


class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            res = x ^ y
            carry = (x & y) << 1
            x, y = res, carry
        return bin(x)[2:]