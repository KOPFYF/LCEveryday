class Solution:
    def expand(self, S: str) -> List[str]:
        n = len(S)
        def dfs(pos, word):
            if pos == n: 
                res.append(word)
                return

            if S[pos] == '{':
                jump = pos + 1
                while S[jump] != '}':
                    jump += 1
                for ch in sorted(S[pos + 1: jump].split(',')):
                    dfs(jump + 1, word + ch)
            else:
                dfs(pos + 1, word + S[pos])
                
        res = []
        dfs(0, "")
        return res