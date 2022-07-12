# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(node):
            if not node:
                return 
            
            if node.val in (startValue, destValue):
                return node
            
            l, r = lca(node.left), lca(node.right)
            if l and r:
                return node
            else:
                return l or r
            
        lca_node = lca(root)
        bfs = deque([(lca_node, '')]) # node, path
        left_path, right_path = '', ''
        
        while bfs:
            node, path = bfs.popleft()
            if node.val == startValue:
                left_path = path
                if right_path:
                    break
            if node.val == destValue:
                right_path = path
                if left_path:
                    break
            
            if node.left:
                bfs.append((node.left, path + 'L'))
            if node.right:
                bfs.append((node.right, path + 'R'))
            
        return len(left_path) * 'U' + right_path