class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        d = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        n, res = len(digits), []
        def dfs(path, i):
            if i == n:
                res.append(path)
                return
            for ch in d[int(digits[i])]:
                dfs(path + ch, i + 1)
        dfs('', 0)
        return res