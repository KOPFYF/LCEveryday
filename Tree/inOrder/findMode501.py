# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return []
        d = defaultdict(int)
        self.helper(root, d)
        max_freq = max(d.values())   
        return [k for k, v in d.items() if v == max_freq]

    def helper(self, root, d):
        if root:
            self.helper(root.left, d)
            d[root.val] += 1
            self.helper(root.right, d)