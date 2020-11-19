# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Inorder traversal of a BST will find the nodes in ascending order
        # The mode will occur in a row
        self.res = []
        self.prev = None
        self.max_count = 0
        self.current_count = 0
        
        self.inorder(root)
        return self.res

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.current_count = 1 if root.val != self.prev else self.current_count + 1
            if self.current_count == self.max_count:
                self.res.append(root.val)
            elif self.current_count > self.max_count:
                self.res = [root.val]
                self.max_count = self.current_count
            self.prev = root.val
            self.inorder(root.right)