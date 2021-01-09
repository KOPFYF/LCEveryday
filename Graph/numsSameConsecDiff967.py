class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        # BFS
        bfs = list(range(10))
        for _ in range(N - 1):
            # bfs = [i * 10 + j for i in bfs for j in {i % 10 - K, i % 10 + K} if i > 0 and 0 <= j < 10]
            nxt = set()
            for i in bfs:
                for j in (i % 10 - K, i % 10 + K):
                    if i > 0 and 0 <= j < 10:
                        nxt.add(i * 10 + j)
            bfs = nxt
        return bfs
    
        # DFS
        def dfs(n: int, num: int, res: List[int]) -> None:
            if n == 1:
                res.append(num) 
            elif num > 0:
                for num2 in [num * 10 + d for d in {num % 10 - K, num % 10 + K} if 0 <= d < 10]:
                    dfs(n - 1, num2, res)
        
        res = []
        for i in range(10):
            dfs(N, i, res)
        return res
    
    
  
        
            