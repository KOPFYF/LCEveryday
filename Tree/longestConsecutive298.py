# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # bottom up DFS, O(n)/O(n)
        self.res = 0
        def dfs(node):
            # use current node as start point, what is the length
            if not node:
                return 0
            length = 1
            l, r = dfs(node.left), dfs(node.right)
            if node.left and node.val == node.left.val - 1:
                length = max(length, l + 1)
            if node.right and node.val == node.right.val - 1:
                length = max(length, r + 1)
            self.res = max(self.res, length) # res could be in the middle
            return length
        
        dfs(root)
        return self.res
            


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # top down DFS, O(n)/O(n)
        # length to store the current consecutive path length
        def dfs(node, parent, length):
            if not node:
                return length

            if parent and node.val == parent.val + 1:
                length += 1
            else:
                length = 1 # reset
            l, r = dfs(node.left, node, length), dfs(node.right, node, length)
            return max(l, r, length)
        
        return dfs(root, None, 0)