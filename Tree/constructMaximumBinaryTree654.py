# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # Cartesian Tree
        
        # recursion, O(n^2)
        def dfs(nums):
            if not nums:
                return None
            root = TreeNode(max(nums))
            i = nums.index(root.val)
            root.left = dfs(nums[:i])
            root.right = dfs(nums[i+1:])
            return root
        
        return dfs(nums)