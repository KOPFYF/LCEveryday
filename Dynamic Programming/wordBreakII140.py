class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # soln 1, pass by s, O(mn)
        n, wordDict = len(s), set(wordDict)
        
        @lru_cache(None)
        def dfs(s):
            if not s: return [[]]
            
            res = []
            for word in wordDict:
                if s.startswith(word):
                    for nxt_word_lst in dfs(s[len(word):]):
                        res.append([word] + nxt_word_lst) 
            return res

        return [" ".join(word) for word in dfs(s)]
    
        # soln 2, pass by index
        n, wordDict = len(s), set(wordDict)
        @lru_cache(None)
        def dfs(pos):
            # return a 2d list of word list using s[pos:]
            if pos == n: return [[]]
            
            res = []
            for i in range(pos, n): # ---pos---i---n
                cand = s[pos:i+1] 
                if cand in wordDict:
                    for nxt_word_lst in dfs(i+1): # try the rest s[i+1:]
                        res.append([cand] + nxt_word_lst)
                        print(res, nxt_word_lst)
            return res
        
        return [" ".join(word) for word in dfs(0)]
        
        # soln 3, cache manully
        memo = {}
        def dfs(s):
            # return a list of words
            if not s:
                return []
            if s in memo:
                return memo[s]
            
            res = []
            for word in wordDict:
                if not s.startswith(word):
                    continue
                if len(word) == len(s):
                    res.append(word)
                else:
                    tmp = dfs(s[len(word):])
                    for item in tmp:
                        item = word + ' ' + item
                        res.append(item)
            # print(res)
            memo[s] = res
            return res
        
        return dfs(s)
