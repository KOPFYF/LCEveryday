# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # tree version of 2 sum, prefix sum + hash table
        res = 0
        cache = collections.defaultdict(int)
        cache[0] = 1 # base case
        
        def dfs(root, cur_sum):
            nonlocal res
            if not root:
                return 
            cur_sum += root.val
            res += cache[cur_sum - sum]
            cache[cur_sum] += 1
            dfs(root.left, cur_sum)
            dfs(root.right, cur_sum)
            # when move to a different branch, the currPathSum is no longer available
            cache[cur_sum] -= 1
          
        dfs(root, 0)
        return res