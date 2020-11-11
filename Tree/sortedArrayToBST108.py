# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """      
#         def _makeBST(nums, l, r):
#             if l > r:
#                 return None
#             if l == r:
#                 return TreeNode(nums[l])
            
#             m = l + (r-l)//2
#             node = TreeNode(nums[m])
#             node.left = _makeBST(nums, l, m-1)
#             node.right = _makeBST(nums, m+1, r)
            
#             return node
        
#         return _makeBST(nums, 0, len(nums)-1)
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root