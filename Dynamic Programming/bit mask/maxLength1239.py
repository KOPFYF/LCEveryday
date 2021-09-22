class Solution:
    def maxLength(self, arr: List[str]) -> int:
        '''
        convert 1111 to 0000
        '''
        # preprocess unvalid words with dup, like this case: ["yy","bkhwmpbiisbldzknpm"]
        arr = [word for word in arr if len(word) == len(set(word)) ]
        masks = []
        for word in arr:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            masks.append(mask)
    
        m = len(masks)
        
        @lru_cache(None)
        def dfs(i, mask):
            # 1111 -> 0000
            if i == m or mask == 0:
                return 0
            res = dfs(i + 1, mask) # no take i
            cur = masks[i]
            if cur & mask == cur:
                nxt_mask = cur ^ mask
                res = max(res, len(arr[i]) + dfs(i + 1, nxt_mask)) # take i
            return res
        
        return dfs(0, (1<<26) - 1)



class Solution2:
    def maxLength(self, arr: List[str]) -> int:
        # DP, bottom up
        dp = [set()]
        for word in arr:
            if len(word) == len(set(word)):
                for used in dp:
                    if not used & set(word):
                        dp.append(used | set(word))
        return len(max(dp, key=len))
        
        # backtracking
        n = len(arr)
        # @lru_cache(None) # set is unhashable
        def dfs(used, pos):
            if pos == n: return 0
            res = dfs(used, pos + 1) # not take
            
            word = arr[pos]
            if len(word) == len(set(word)) and not used & set(word):
                res = max(res, len(word) + dfs(used | set(word), pos + 1))
            
            return res
        
        return dfs(set(), 0)