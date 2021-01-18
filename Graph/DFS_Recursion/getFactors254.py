class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n == 1:
            return []
        res = []
        def dfs(path, idx, target):
            if path: # res path is at least 2 elements
                res.append(path + [target])
            for i in range(idx, int(target**0.5 + 1)):
                if target % i == 0:
                    dfs(path + [i], i, target // i)
        dfs([], 2, n)
        
        return res