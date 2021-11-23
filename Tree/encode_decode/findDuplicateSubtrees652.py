# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # O(n) / O(n)
        tree_pattern_count = defaultdict(int)
        res = []
        
        def serilize(node):
            if not node:
                return '#'
            encode = str(node.val) + ',' + serilize(node.left) + ',' + serilize(node.right)
            if tree_pattern_count[encode] == 1: # seen this pattern before
                res.append(node)
            tree_pattern_count[encode] += 1
            return encode
        
        serilize(root)
        print(tree_pattern_count)
        return res