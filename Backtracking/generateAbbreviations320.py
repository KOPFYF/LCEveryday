class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        # dfs + memo
        n = len(word)
        res = []
        @functools.lru_cache(None)
        def dfs(pos, path, cnt):
            if pos == n: 
                res.append(path + str(cnt) if cnt > 0 else path)
                return
            # turn current char to integer
            dfs(pos + 1, path, cnt + 1) 
            # take current char as str path, wrap up prev cnt
            dfs(pos + 1, path + (str(cnt) if cnt else "") + word[pos], 0)
            
        dfs(0, "", 0)
        return res
    
    
        # backtracking O(2 ^ n)
        n = len(word)
        res = []
        def dfs(pos, word, path, cnt):
            if pos == n: 
                res.append(path + str(cnt) if cnt > 0 else path)
                return
            # turn current char to integer
            dfs(pos + 1, word, path, cnt + 1) 
            # take current char as str path, wrap up prev cnt
            dfs(pos + 1, word, path + (str(cnt) if cnt else "") + word[pos], 0)
            
        dfs(0, word, "", 0)
        return res
            
            