# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list) # key: 1 to max_depth
        def depth(node):
            # return depth for current node
            if not node:
                return 0
            l, r = depth(node.left), depth(node.right)
            cur_depth = max(l, r) + 1
            dic[cur_depth].append(node.val)
            return cur_depth
        
        depth(root)
        # print(dic)
        
        res = []
        for k in range(1, len(dic) + 1):
            res.append(dic[k])
        return res