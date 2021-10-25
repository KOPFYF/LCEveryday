class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        
        while a or b:
            if len(res) >= 2 and res[-1] == res[-2]:
                write_a = res[-1] == 'b'
            else:
                write_a = a >= b # greedy
            
            if write_a:
                res.append('a')
                a -= 1
            else:
                res.append('b')
                b -= 1
        
        return "".join(res)
            