# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        # soln 1
        memos = {}
        def dfs(N, memos):
            if N in memos: return memos[N]
            if N == 1: return [TreeNode(0)] # base case
            res = []
            for l in range(1, N, 2): # Only odd number can form a full binary tree
                for left in self.allPossibleFBT(l):
                    for right in self.allPossibleFBT(N - l - 1):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        res += [root]
            memos[N] = res
            return res
        return dfs(N, memos)
        
        # soln 2
        from itertools import product
        @lru_cache(None)
        def build(n):
            if n == 1:
                return [TreeNode(0)]
            
            return [TreeNode(0, left, right) for i in range(1, n - 1)
                    for left, right in product(build(i), build(n - i - 1))]
        
        return build(N)