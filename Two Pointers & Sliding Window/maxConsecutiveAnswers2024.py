class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        # either change T to F, or F to T, no mix
        res1, i, cnt = 0, 0, 0
        for j in range(len(s)):
            cnt += s[j] == 'T'
            while cnt > k:
                cnt -= s[i] == 'T'
                i += 1
            res1 = max(res1, j - i + 1)  
            
        res2, i, cnt = 0, 0, 0
        for j in range(len(s)):
            cnt += s[j] == 'F'
            while cnt > k:
                cnt -= s[i] == 'F'
                i += 1
            res2 = max(res2, j - i + 1) 
        
        return max(res1, res2)
    
        # same idea, written in a seperate function
        def longestWin(c: str) -> int:
            lo, win, cnt = -1, 0, 0
            for hi in range(len(key)):
                if key[hi] == c:
                    cnt += 1
                while cnt > k:
                    lo += 1
                    if key[lo] == c:
                        cnt -= 1
                win = max(win, hi - lo)
            return win     
        
        return max(map(longestWin, ('T', 'F')))