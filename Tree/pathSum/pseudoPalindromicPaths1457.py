# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution0:
    # 800 ms
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        # soln 0, bit mask
        # Use the 0th to 9th bits of a int to record the odd/even frequency in a path
        def preorder(node, cnt):
            if not node:
                return 0
            cnt ^= 1 << node.val
            if not node.left and not node.right:
                return 0 if bin(cnt).count('1') > 1 else 1
            return preorder(node.left, cnt) + preorder(node.right, cnt)
        return preorder(root, 0)

class Solution1:
    # 1000 ms
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def preorder(node, cnt):
            if not node:
                return 0
            cnt[node.val] += 1
            if not node.left and not node.right: # reach leaf
                return 1 if sum(c % 2 for c in cnt) < 2 else 0
            l, r = preorder(node.left, cnt[:]), preorder(node.right, cnt[:])
            return l + r
        
        return preorder(root, [0] * 10)


class Solution_TLE:
    # 53/56
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def isLeaf(node):
            return node.left is None and node.right is None
        
        paths = []
        def helper(root, path):
            if not root:
                return 
            if isLeaf(root):
                paths.append(path + [root.val])
            helper(root.left, path + [root.val])
            helper(root.right, path + [root.val])   
        
        def isPseudoPalind(ls):
            d = Counter(ls)
            odd = 0
            for cnt in d.values():
                if cnt % 2:
                    odd += 1
                    if odd > 1:
                        return False
            return True
        
        helper(root, [])
        res = 0
        for path in paths:
            if isPseudoPalind(path):
                res += 1
        return res
            