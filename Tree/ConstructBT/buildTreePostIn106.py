# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # soln 1
        if inorder:
            root = TreeNode(postorder.pop())
            i = inorder.index(root.val)
            # must deal with right first, cause it's postorder and we pop from right to left
            root.right = self.buildTree(inorder[i+1:], postorder)
            root.left = self.buildTree(inorder[:i], postorder)
            return root
        
        # soln 2, Time O(n), Space O(n)
        hashmap = {num: i for i, num in enumerate(inorder)}

        def helper(l, r):
            # Given a range, find the root
            if l > r:
                return None
            x = TreeNode(postorder.pop()) # find root from postorder
            idx = hashmap[x.val] # find root idx in inorder and split left/right
            # must deal with right first, cause it's postorder and we pop from right to left
            x.right = helper(idx + 1, r)
            x.left = helper(l, idx - 1)    
            return x
        
        return helper(0, len(inorder) - 1)
    