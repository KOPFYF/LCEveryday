class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        graph = collections.defaultdict(list)
        for i in range(nodes):
            if parent[i] != -1:
                graph[parent[i]].append(i)
        
        @cache
        def dfs(node):
            # dfs bottom up
            # return (tree sum, # tree nodes)
            runsum = value[node]
            cnt = 1
            for child in graph[node]:
                child_sum, child_cnt = dfs(child)
                runsum += child_sum
                cnt += child_cnt
            
            if runsum == 0:
                cnt = 0
            return runsum, cnt
        
        return dfs(0)[1]