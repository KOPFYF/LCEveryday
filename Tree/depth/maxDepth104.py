# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # BFS
        if not root: return 0
        depth = 0
        queue = deque([root])
        while queue:
            depth += 1
            # BFS deal with all cur nods in level, 精髓在于for loop
            for i in range(len(queue)):
                c = queue.popleft()
                if c.left:
                    queue.append(c.left)
                if c.right:
                    queue.append(c.right)
        return depth
    
        # DFS
        if not root: return 0
        def dfs(root):
            if root:
                return 1 + max(dfs(root.left), dfs(root.right))
            else:
                return 0
        return dfs(root)
        
        
            