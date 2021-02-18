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


class Solution2:
    # take or to take
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.helper(root, sum, True)

    def helper(self, root, subtarget, origin):
        if not root: return 0
        res = 0
        if root.val == subtarget:
            res += 1
        left = self.helper(root.left, subtarget-root.val, False)
        right = self.helper(root.right, subtarget-root.val, False)
        if origin:
            left += self.helper(root.left, subtarget, origin)
            right += self.helper(root.right, subtarget, origin)
        return res + left + right