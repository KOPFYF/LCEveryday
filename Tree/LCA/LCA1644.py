# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/discuss/1011154/Failed-This-Question-In-Two-Mock-Interview-So-Post-This-To-Remind-myself-specifically

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.cnt = 0

        lca = self.dfs(root, p, q)
        if self.cnt == 2:
            return lca
        else:
            return None
         
    def dfs(self, root, p, q):
        if not root:
            return None

        # in V1, we instantly returned the p / q when we sees it for the base case here
        # recursion here is for finding p and q node! Not for finding the LCA!
        # we cannot instantly return the node we found here because we don't know if all m and n exist in the tree
        l = self.dfs(root.left, p, q)
        r = self.dfs(root.right, p, q)

        if root in (p, q):
            self.cnt += 1 # Once we found either one, we will have  to update counter
            return root

        if l and r: # left side and right side both found targets
            return root
        if l:
            return l
        if r:
            return r
        return None


class Solution:        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':       
        self.flagp = False
        self.flagq = False
        res = self.helper(root, p, q)
        if not self.flagp or not self.flagq: 
            return None
        return res
        
    def helper(self, root, p, q):
        if not root:
            return None
        left, right = self.helper(root.left, p, q), self.helper(root.right, p, q)
        if root == p:
            self.flagp = True
            return root
        if root == q:
            self.flagq = True
            return root 
        if left and right:
            return root
        if left or right:
            return right or left


class Solution_run_3_times:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = self.dfs(root, p, q)
        lca_p = self.dfs(root, p, p)
        lca_q = self.dfs(root, q, q)
        if lca and lca_p and lca_q:
            return lca
        else:
            return None
        
         
    def dfs(self, root, p, q):
        if not root:
            return None
        if root in (p, q):
            return root

        l = self.dfs(root.left, p, q)
        r = self.dfs(root.right, p, q)

        if l and r:
            return root
        if l:
            return l
        if r:
            return r
        return None