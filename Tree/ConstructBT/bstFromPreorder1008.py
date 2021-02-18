# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        # soln 0, O(n^2), Find the left part and right part, then recursively construct the tree.
        if not preorder: return None
        root = TreeNode(preorder[0])
        i = bisect.bisect(preorder, preorder[0])
        # print(preorder[0], i)
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
    
        # soln 1, O(nlogn)
        def helper(i, j):
            if i == j: return None
            root = TreeNode(A[i])
            mid = bisect.bisect(A, A[i], i + 1, j)
            root.left = helper(i + 1, mid)
            root.right = helper(mid, j)
            return root
        return helper(0, len(A))
        
        # soln 2
        # https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/discuss/252232/JavaC%2B%2BPython-O(N)-Solution
        return self.buildTree(A[::-1], float('inf'))

    def buildTree(self, A, bound):
        if not A or A[-1] > bound: return None
        node = TreeNode(A.pop())
        node.left = self.buildTree(A, node.val)
        node.right = self.buildTree(A, bound)
        return node
        
        # soln 3, use code from p105, O(n^2)
        inorder = sorted(preorder)
        return self.buildTree(preorder, inorder)
        
    def buildTree(self, preorder, inorder):
        # soln 3
        if inorder:
            root = TreeNode(preorder.pop(0))
            i = inorder.index(root.val)
            root.left = self.buildTree(preorder, inorder[:i])
            root.right = self.buildTree(preorder, inorder[i+1:])
            return root