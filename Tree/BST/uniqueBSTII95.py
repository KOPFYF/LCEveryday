# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # F(i, n) = G(i-1) * G(n-i)	1 <= i <= n 
    # G(n) = F(1, n) + F(2, n) + ... + F(n, n). 
    # G(n) = G(0) * G(n-1) + G(1) * G(n-2) + … + G(n-1) * G(0) 
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.generate(1, n)
    
    def generate(self, start, end):
        if start > end:
            return [None]
        res = []
        for root in range(start, end + 1):
            leftSubTree = self.generate(start, root - 1)
            rightSubTree = self.generate(root + 1, end)
            for nodeLeft in leftSubTree:
                for nodeRight in rightSubTree:
                    temp = TreeNode(root)
                    temp.left = nodeLeft
                    temp.right = nodeRight
                    res.append(temp)
        return res