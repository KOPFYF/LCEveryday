'''
dp bitmask
knapsack

dp的大循环就是 for (state=0; state<(1<<n); state++). 对于该状态state，我们尝试每一个sticker[k]，计算状态i经过sticker[k]的帮助后得到的状态new_state（注意已经分析过new_state肯定是大于state的），那么dp[new_state]就可以得到更新dp[new_state]=min(dp[new_state], dp[state]+1)
'''
class Solution_bitmask_bottom_up:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # bottom up
        n = len(target)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        
        def findNextMask_wrong(mask, target, sticker):
            # O(wn), w is the word length
            nxt_mask = mask
            for ch in sticker:
                for i in range(n): # check each bit of target
                    if mask & (1 << i) == 0 and target[i] == ch: # i-th not visited & matched
                        nxt_mask = mask ^ (1 << i)
                        break
            return nxt_mask
        
        def findNextMask_wrong2(mask, target, sticker):
            # O(wn), w is the word length
            bk = False
            for j in range(len(sticker)):
                for i in range(n): # check each bit of target
                    if mask & (1 << i) == 0 and target[i] == sticker[j]: # i-th not visited & matched
                        mask = mask ^ (1 << i)
                        bk = True
                        break
                if bk:
                    break
            return mask
        
        def findNextMask(mask, target, sticker):
            # O(wn), w is the word length
            for ch in sticker:
                for i in range(n): # check each bit of target
                    if mask & (1 << i) == 0 and target[i] == ch: # i-th not visited & matched
                        mask = mask ^ (1 << i)
                        break
            return mask
        

        # convert 0000 to 1111
        for mask in range(1<<n):
            if dp[mask] == float('inf'):
                continue # skip invalid base cases
            for sticker in stickers:
                # convert from mask to next mask using one sticker
                nxt_mask = findNextMask(mask, target, sticker)
                dp[nxt_mask] = min(dp[nxt_mask], dp[mask] + 1)
        # print(dp)
        return dp[(1<<n) - 1] if dp[(1<<n) - 1] != float('inf') else -1


class Solution_bitmask_top_down:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        full_mask = (1 << n) - 1
        ls_map = [Counter(s) for s in stickers]
        
        @lru_cache(None)
        def dfs(mask):
            # 0000 -> 1111
            if mask == full_mask:
                return 0
            
            res = 51
            for cnt in ls_map: # length of s
                nxt_mask = mask
                for i in range(n):
                    if mask & (1 << i) == 0 and cnt[target[i]] > 0:
                        nxt_mask = mask ^ (1 << i)
                        cnt[target[i]] -= 1
                if nxt_mask != mask:
                    res = min(res, 1 + dfs(nxt_mask))
            
            return res
        
        res = dfs(0)
        return res if res != 51 else -1