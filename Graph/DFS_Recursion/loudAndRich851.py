class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # For person i, remember the quietest person who is richer than person i.
        # dfs + memo 
        n = len(quiet)
        graph = defaultdict(set)
        for x, y in richer:
            # x > y, it means y go to x
            graph[y].add(x)
        
        res = [-1] * n # memo
        def dfs(i):
            if res[i] != -1:
                return 
            res[i] = i # base case is himself, with equal money and quietness
            for j in graph[i]:
                dfs(j)
                if quiet[res[i]] > quiet[res[j]]: # j is richer but quieter
                    res[i] = res[j]
        
        for i in range(n):
            dfs(i)
        
        return res