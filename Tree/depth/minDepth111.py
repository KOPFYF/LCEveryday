# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # DFS
        if (root == None):	return 0
        # only left or right child exists
        if (root.left == None):	return self.minDepth(root.right) + 1
        if (root.right == None): return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        
        # BFS
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    # reach leave
                    return level
                else:
                    queue.append((node.left, level + 1))
                    queue.append((node.right, level + 1))