# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        # > 类型：DFS
        # > Time Complexity O(N)
        # > Space Complexity O(H)
        # 第一种比如在node为4的这一层，我们要做的是将4的root.left = 3
        # 第二种比如在node为2的这一层，我们要做的是将2的root.right = None
        if not root: return [None, None]
        
        if root.val > target:
            # target is on the root.left, keep the right subtree
            left, right = self.splitBST(root.left, target)
            root.left = right
            return [left, root]
        else:
            left, right = self.splitBST(root.right, target)
            root.right = left
            return [root, right]