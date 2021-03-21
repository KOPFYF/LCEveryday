# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        # 1. Convert the tree to a sorted array using an in-order traversal.
        # 2. Construct a new balanced tree from the sorted array recursively.
        res = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)   
        inorder(root)

        def build(res):
            if not res:
                return None
            mid = len(res) // 2
            root = TreeNode(res[mid])
            root.left = build(res[:mid])
            root.right = build(res[mid+1:])
            return root
        
        def build_tree(i, j):
            # passed by index
            if i > j:
                return None
            m = (i + j) // 2
            root = TreeNode(res[m])
            root.left = build_tree(i, m - 1)
            root.right = build_tree(m + 1, j)
            return root
        
        return build_tree(0, len(res) - 1)
        # return build(res)
            