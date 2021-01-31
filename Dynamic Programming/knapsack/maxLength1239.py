class Solution:
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
                res = max(res, len(word) + dfs(used | set(word), pos + 1)) # take
            
            return res
        
        return dfs(set(), 0)
            