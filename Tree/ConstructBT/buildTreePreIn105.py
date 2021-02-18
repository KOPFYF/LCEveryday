# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # soln 1
        if inorder:
            root = TreeNode(preorder.pop(0))
            i = inorder.index(root.val)
            root.left = self.buildTree(preorder, inorder[:i])
            root.right = self.buildTree(preorder, inorder[i+1:])
            return root
        
        
        # soln 2
        hashmap = {num: i for i, num in enumerate(inorder)}

        def helper(l, r):
            # Given a range, find the root
            if l > r:
                return None
            x = TreeNode(preorder.pop(0)) # find root from preorder
            idx = hashmap[x.val] # find root idx in inorder and split left/right
            # must deal with left first, cause it's preorder
            x.left = helper(l, idx - 1)   
            x.right = helper(idx + 1, r)
            return x