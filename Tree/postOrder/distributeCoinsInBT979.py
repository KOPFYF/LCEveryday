# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        # postOrder, traverses the tree bottom up
        self.res = 0
        def postOrder(root):
            if not root:
                return 0
            left, right = postOrder(root.left), postOrder(root.right)
            self.res += abs(left) + abs(right) # accumulate the abs value of traffic
            # keep one coin for the root, return the sum
            return root.val + left + right - 1
        
        postOrder(root)
        return self.res