class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp + Last Set Bit
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        return ans 
    
        # find rightmost 1-bit
        def countOne(x):
            cnt = 0
            while x:
                x = x & (x - 1) # turn off the rightmost 1-bit
                cnt += 1
            return cnt
        
        return [countOne(x) for x in range(n+1)]