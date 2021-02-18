# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution0:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def dfs(node, target):
            if not node:
                return False
            if not node.left and not node.right and node.val == target:
                return True
            return dfs(node.left, target - node.val) or dfs(node.right, target - node.val)
        
        return dfs(root, sum)


class Solution1(object):
    def hasPathSum(self, root, sum):
        res = []
        self.dfs(root, sum, res)
        return any(res)

    def dfs(self, root, target, res):
        if root:
            if root.left == None and root.right == None:
                # reach leave nodes and left = right = null
                if root.val == target:
                    res.append(True)
            if root.left:
                self.dfs(root.left, target - root.val, res)
            if root.right:
                self.dfs(root.right, target - root.val, res)



class Solution2(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True  
        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

