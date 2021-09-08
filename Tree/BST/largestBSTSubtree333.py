# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = 1
        def dfs(node):
            # return BST flag, min, max and cnt if BST
            if not node:
                return True, 10001, -10001, 0
            lBST, lmin, lmax, lcnt = dfs(node.left)
            rBST, rmin, rmax, rcnt = dfs(node.right)
            if lBST and rBST and lmax < node.val < rmin:
                cnt = lcnt + rcnt + 1
                self.res = max(self.res, cnt)
                # print(lmin, lmax, node.val, rmin, rmax)
                # return True, lmin, rmax, cnt # why wrong? bcz init min as 10001, max as -10001, now to reset to normal
                return True, min(lmin, node.val), max(node.val, rmax), cnt
            else:
                # return False, 0, 0, 0 # I dont care this part 
                return False, -10001, 10001, 0
        
        dfs(root)
        return self.res