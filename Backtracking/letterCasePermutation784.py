class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        n = len(S)
        res = []
        def dfs(pos, path):
            if pos == n:
                res.append(path)
                return
            if S[pos].isdigit():
                dfs(pos + 1, path + S[pos])
            else:
                dfs(pos + 1, path + str.lower(S[pos]))
                dfs(pos + 1, path + str.upper(S[pos]))
            
        dfs(0, "")
        return res