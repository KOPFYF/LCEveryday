# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        # DFS bottom up + hash
        def dfs(root, d):
            if not root:
                return 0
            left = dfs(root.left, d)
            right = dfs(root.right, d)
            depth = max(left, right) + 1
            d[depth] += root.val,
            return depth
        d, res = collections.defaultdict(list), []
        dfs(root, d)
        # print(d, res)
        for i in range(1, len(d) + 1):
            res.append(d[i])
        return res

        
        res = []
        def dfs(root):
            # take the maximum of the depth from left child and right child
            if not root: return 0
            depth = max(dfs(root.left), dfs(root.right)) + 1
            if len(res) < depth: 
                # prevent index overflow, make sure res[depth - 1] is valid
                res.append([])
            res[depth - 1].append(root.val)
            return depth
        
        dfs(root)
        return res