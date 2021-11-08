


class Solution:
    def countBits(self, n: int) -> List[int]:
        # DP, O(n) / O(1), P(x)=P(x/2)+(xmod2)
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            # x // 2 is x >> 1 and x % 2 is x & 1
            ans[x] = ans[x >> 1] + (x & 1) 
        return ans


        # dp + Last Set Bit
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1 # x & (x - 1) turn off the rightmost 1
        return ans 
    
        # find rightmost 1-bit
        @cache
        def countOne(x):
            cnt = 0
            while x:
                x = x & (x - 1) # turn off the rightmost 1-bit
                cnt += 1
            return cnt
        
        return [countOne(x) for x in range(n+1)]