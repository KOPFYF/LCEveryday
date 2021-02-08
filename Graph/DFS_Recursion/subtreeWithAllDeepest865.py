# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        '''
        if root == null,
        return pair(0, null)

        if left depth == right depth,
        deepest nodes both in the left and right subtree,
        return pair (left.depth + 1, root)

        if left depth > right depth,
        deepest nodes only in the left subtree,
        return pair (left.depth + 1, left subtree)

        if left depth < right depth,
        deepest nodes only in the right subtree,
        return pair (right.depth + 1, right subtree)

        '''
        def dfs(root):
            # return max depth and subtree node
            if not root:
                return 0, None
            (l_depth, l_node), (r_depth, r_node) = dfs(root.left), dfs(root.right)
            if l_depth > r_depth:
                return l_depth + 1, l_node
            elif l_depth < r_depth:
                return r_depth + 1, r_node
            else:
                return l_depth + 1, root
        return dfs(root)[-1]