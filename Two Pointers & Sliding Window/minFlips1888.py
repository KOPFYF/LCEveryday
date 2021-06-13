class Solution:
    def minFlips(self, s: str) -> int:
        # sliding win, O(n)/O(n)
        n = len(s)
        t1, t2 = '10'*n, '01'*n
        d1, d2, ans = 0, 0, n
        for i in range(2*n):
            if s[i%n] != t1[i]: 
                d1 += 1
            if s[i%n] != t2[i]: 
                d2 += 1
            if i >= n:
                # the most left element is outside of sliding window,
                # we need to subtract the ans if we did `flip` before
                if s[i-n] != t1[i-n]: 
                    d1 -= 1
                if s[i-n] != t2[i-n]: 
                    d2 -= 1
            if i >= n-1:
                ans = min(d1, d2, ans)
        return ans
        
        
        # O(n^2) TLE
        n = len(s)
        s2 = s + s # circular
        cmp1 = '10' * (n//2) + ('1' if (n//2 == 1) else '')
        cmp2 = '01' * (n//2) + ('0' if (n//2 == 1) else '')
        
        # print(s, s2, n, cmp1, cmp2)
        res = float('inf')
        for i in range(n):
            s3 = s2[i:i+n]
            cnt1 = 0
            for x, y in zip(s3, cmp1):
                if x != y:
                    cnt1 += 1
            res = min(res, cnt1)
            
            cnt2 = 0
            for x, y in zip(s3, cmp2):
                if x != y:
                    cnt2 += 1
            res = min(res, cnt2)
        
        return res
            
                    
                    
            