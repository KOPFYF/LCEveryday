# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        # dfs + hash table
        if not root: return []
        d = defaultdict(int)
        
        # @lru_cache(None)
        def dfs(root):
            if not root: return 0
            s = root.val + dfs(root.left) + dfs(root.right)
            d[s] += 1
            return s
        
        dfs(root)
        maxCount = max(d.values())
        return [s for s in d if d[s] == maxCount]