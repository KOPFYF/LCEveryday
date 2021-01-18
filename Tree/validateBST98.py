# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, low, high):
            if not root:
                return True
            if root.val <= low or root.val >= high:
                return False
            return helper(root.left, low, root.val) and helper(root.right, root.val, high)
        
        return helper(root, float("-inf"), float("inf"))


class Solution2(object):
    def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
        if not root: 
            # reach leaf node and return True
            return True
        if root.val <= floor or root.val >= ceiling:
            return False
        # in the left branch, root is the new ceiling; contrarily root is the new floor in right branch
        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)