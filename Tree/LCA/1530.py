# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    dist_from_leaf1_to_LCA + dist_from_leaf2_to_LCA <= distance
    count += sum(l + r <= distance for l in left for r in right)
    '''
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # lca
        res = 0
        def dfs(node):
            # bottom up
            # [dist] from current node to all leaves
            # only cache dist if the depth < distance
            nonlocal res
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            ls, rs = dfs(node.left), dfs(node.right)
            res += sum(l + r <= distance for l in ls for r in rs)
            return [n + 1 for n in ls + rs if n + 1 < distance] # pruning
        
        dfs(root)
        return res
        