# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # DFS to build graph, then BFS to do level traverse
        graph = defaultdict(list)
        def dfs(node, graph):
            if not node:
                return 
            if node.left:
                graph[node.val].append(node.left.val) # undirected edge
                graph[node.left.val].append(node.val) # undirected edge
                dfs(node.left, graph)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right, graph)
        dfs(root, graph)
        # print(graph)
        
        bfs = [target.val]
        level = 0
        seen = set([target.val]) # the starting node is the target, it is the root
        while bfs:
            nxt_bfs = []
            if level == K:
                return bfs
            for node in bfs:
                for nxt_node in graph[node]:
                    if nxt_node not in seen:
                        nxt_bfs.append(nxt_node)
                        seen.add(nxt_node)
            bfs = nxt_bfs
            level += 1
        return []