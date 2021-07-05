# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
It's using pre-order for left boundary , in-order for bottom boundary (because it's basically sea-sawing the bottom) and post-order (but going right node first) for right boundary
'''
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        boundary = [root.val]
        
        def dfs_left(node):
            # pre-order
            if not node or not node.left and not node.right:
                return
            boundary.append(node.val)
            if node.left:
                dfs_left(node.left)
            else:
                dfs_left(node.right)
                
        def dfs_leaves(node):
            if not node:
                return
            dfs_leaves(node.left)
            if node != root and not node.left and not node.right:
                boundary.append(node.val)
            dfs_leaves(node.right)
            
        def dfs_right(node):
            # post-order
            if not node or not node.left and not node.right:
                return
            if node.right:
                dfs_right(node.right)
            else:
                dfs_right(node.left)
            boundary.append(node.val)
            
        dfs_left(root.left)
        # print(boundary)
        dfs_leaves(root)
        # print(boundary)
        dfs_right(root.right)
        # print(boundary)
        
        return boundary


# https://leetcode.com/problems/boundary-of-binary-tree/discuss/101307/Python-solution-recursive-dfs-~20-lines.
class Solution1:
    def boundaryOfBinaryTree(self, root):
        # The main idea is to carry the flag isleft and isight
        # in the dfs steps to help decide when to add node
        # values to the boundary array.
        if not root: 
            return []
        boundary = [root.val]
        def dfs(root, isleft, isright):
            if root:
                # append when going down from the left or at leaf node
                if (not root.left and not root.right) or isleft:
                    boundary.append(root.val)
                
                if root.left and root.right:
                    dfs(root.left, isleft, False)
                    dfs(root.right, False, isright)
                else:
                    dfs(root.left,  isleft, isright)
                    dfs(root.right, isleft, isright)
                
                # append to boundary when coming up from the right
                if (root.left or root.right) and isright:
                    boundary.append(root.val)
        
        dfs(root.left, True, False)
        dfs(root.right, False, True)
        return boundary


class Solution2:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        rslt = []
        # root
        rslt.append(root.val)
        if not root.left and not root.right:
            return rslt
        # left boundary
        if root.left:
            left = root.left
            while left.left or left.right:
                rslt.append(left.val)
                left = left.left if left.left else left.right
        # leaves
        stack = [root]
        while stack:
            temp = stack.pop()
            if not temp.left and not temp.right:
                rslt.append(temp.val)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        # right boundary
        temp = []
        if root.right:
            right = root.right
            while right.right or right.left:
                temp.append(right.val)
                right = right.right if right.right else right.left
        return rslt + temp[::-1]



