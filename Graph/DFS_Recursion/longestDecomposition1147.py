class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        base = 26
        nums = [ord(text[i]) - ord('a') for i in range(n)]
        
        def dfs(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            
            res = 1
            for k in range(1, (j - i + 1) // 2 + 1):
                if text[i: i + k] == text[j - k + 1:j + 1]:
                    res = 2 + dfs(i + k, j - k)
                    break
            return res
        
        return dfs(0, n - 1)