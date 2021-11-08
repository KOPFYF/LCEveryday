class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # TLE on the last case
        # use cache and dont use Counter but tuple as counter
        cnt = Counter(target)
        self.res = float('inf')
        n = len(target)
        
        def dfs(dic, used, i):
            # for target[i:], how many stickers we need
            if i == n:
                self.res = min(self.res, used)
            elif dic[target[i]] >= cnt[target[i]]:
                dfs(dic, used, i + 1)
            # elif used < self.res - 1:
            else:
                for sticker in stickers:
                    if target[i] in sticker:
                        for s in sticker: 
                            dic[s] += 1
                        dfs(dic, used + 1, i + 1)
                        for s in sticker: 
                            dic[s] -= 1
        
        dic = defaultdict(int)
        dfs(dic, 0, 0)
        
        return self.res if self.res < float("inf") else -1




class Solution(object):
    def minStickers(self, stickers, target):
        m = len(stickers)
        mp = [[0]*26 for y in range(m)] 
        for i in range(m):
            for c in stickers[i]:
                mp[i][ord(c)-ord('a')] += 1    
        dp = {}
        dp[""] = 0
        
        def helper(dp, mp, target):
            if target in dp:
                return dp[target]
            n = len(mp)
            tar = [0]*26
            for c in target:
                tar[ord(c)-ord('a')] += 1   
            ans = sys.maxint
            for i in xrange(n):
                if mp[i][ord(target[0])-ord('a')] == 0:
                    continue
                s = ''
                for j in range(26):
                    if tar[j] > mp[i][j]:
                        s += chr(ord('a')+j)*(tar[j] - mp[i][j]) 
                tmp = helper(dp, mp, s)
                if (tmp != -1): 
                    ans = min(ans, 1+tmp)    
            dp[target] = -1 if ans == sys.maxint else ans
            return dp[target]
                
        return helper(dp, mp, target)