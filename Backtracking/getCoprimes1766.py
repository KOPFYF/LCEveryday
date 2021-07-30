class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        # 1 <= nums[i] <= 50
        n, res = len(nums), [-1] * len(nums)
        # path[x] contains list of nodes from root to current node which their node's value are equal to x
        path = [[] for _ in range(51)] # store (node, depth)
        graph, seen = defaultdict(list), set()
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(node, depth):
            # find closest ancestor for current node
            if node in seen:
                return
            seen.add(node)
            largestDepth = -1
            for x in range(1, 51): # check all candidates
                if gcd(nums[node], x) == 1 and path[x]: # node & x are coprime 
                    closetNode, closetDepth = path[x][-1]
                    if largestDepth < closetDepth: # update optimal soln for each x
                        largestDepth = closetDepth
                        res[node] = closetNode
            # backtracking
            path[nums[node]].append((node, depth))
            for nxt in graph[node]:
                dfs(nxt, depth + 1)
            path[nums[node]].pop()
                        
                
        dfs(0, 0)
        return res
                    
                    
                    
            